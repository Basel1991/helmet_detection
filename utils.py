"""
Author: Basel Alyafi
Date: 23/05/2021
"""
import json
import subprocess
import http.client
import cv2
import imutils
import numpy as np
import os
import time

def down_sample(json_params):
    """
    This function down-samples a video (given the video_path in the passed JSON file)
    It sets the fps (frames per second) to five by default.
    :param file_path: str, the path to the JSON parameters file
    :return: void
    """

    # read the path to the video and the path where to save the down-sampled version
    video_path = json_params['video_path']
    dsampled_path = json_params['new_video_path']
    width = json_params['new_video_width']

    # this height is to keep the same aspect ratio
    height = -2
    new_fps = json_params['new_video_fps']

    command = f'ffmpeg -i "{video_path}" -r {new_fps}  -filter:v scale={width}:{height} "{dsampled_path}"'

    # call the command using shell
    subprocess.call(command, shell=True)
    print(command)

def detect_helmet(params):
    """
    This functions uses DarkNet from OpenCV to detect helmets in videos.
    This script was adopted and modified from the GitHub repository https://github.com/AyazSaiyed/Helmet-Detection- (Developer -        Ayaz Saiyed M.)

    :param params: parameters data dictionary
    :return: frames and coordinates of helmet locations (TODO)
    """
    # load the COCO class labels this YOLO model was trained on
    labelsPath = os.path.sep.join([params["yolo"], "cocohelmet.names"])
    LABELS = open(labelsPath).read().strip().split("\n")

    # initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
                               dtype="uint8")

    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join([params["yolo"], "yolov3-obj_2400.weights"])
    configPath = os.path.sep.join([params["yolo"], "yolov3-obj.cfg"])

    # load our YOLO object detector trained on COCO dataset (80 classes)
    # and determine only the *output* layer names that we need from YOLO
    print("Ready to Load")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # initialize the video stream, pointer to output video file, and
    # frame dimensions - uncomment below line if inputting a video file rather than webcam.
    vs = cv2.VideoCapture(params["new_video_path"])

    writer = None
    (W, H) = (None, None)

    # try to determine the total_frames number of frames in the video file
    try:
        prop = cv2.cv.CV_CAP_PROP_FRAME_COUNT if imutils.is_cv2() \
            else cv2.CAP_PROP_FRAME_COUNT
        total_frames = int(vs.get(prop))
    # print("{} total_frames frames in video".format(total_frames))

    # an error occurred while trying to determine the total_frames
    # number of frames in the video file
    except:
        print("could not determine # of frames in video")
        print("no approx. completion time can be provided")
        total_frames = -1

    # loop over frames from the video file stream
    for frame_idx in range(total_frames):

        print(f"Frame {frame_idx}/{total_frames - 1}")

        # read the frames one by one using cv2
        _, frame = vs.read()
        frame_idx += 1

        # if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]

        # construct a blob from the input frame and then perform a forward
        # pass of the YOLO object detector, giving us our bounding boxes
        # and associated probabilities
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                     swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()

        # initialize our lists of detected bounding boxes, confidences,
        # and class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability)
                # of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > params["confidence"]:
                    # scale the bounding box coordinates back relative to
                    # the size of the image, keeping in mind that YOLO
                    # actually returns the center (x, y)-coordinates of
                    # the bounding box followed by the boxes' width and
                    # height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top
                    # and and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates,
                    # confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        # apply non-maxima suppression to suppress weak, overlapping
        # bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, params["confidence"],
                                params["threshold"])

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                # draw a bounding box rectangle and label on the frame
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                                           confidences[i])
                cv2.putText(frame, text, (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                print("I just found", text)

        # checking if the video writer is None
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(params["output"], fourcc, params["new_video_fps"],
                                     (frame.shape[1], frame.shape[0]), True)

            # some information on processing single frame
            if total_frames > 0:
                elap = (end - start)
                print("[INFO] single frame took {:.4f} seconds".format(elap))
                print("[INFO] estimated total_frames time to finish: {:.4f}".format(elap * total_frames))

        # do a bit of cleanup
        cv2.destroyAllWindows()

        # write the output frame to disk
        writer.write(frame)

    # release the file pointers
    print("Cleaning up the stuff...")
    writer.release()
    vs.release()


def post_request(url, data_dict):
    conn = http.client.HTTPSConnection(url)
    conn.request("POST", "/", str(data_dict), {'Content-Type': 'application/json'})