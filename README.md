# helmet_detection
Detecting helmets in a video using YOLO v3.

The steps that were followed to complete this task were as follows:

# 1. Video Downsampling
In this step, ffmpeg is used to scale (down or up) a given video. The parameters are all passed in the params.txt file (JSON format).

Examples of the parameters' values are given below:
 * ## Video Down-sampling Section
   Parameter|Value|Meaning
   ---------|-----|-------
    "video_path"| "./videos/video.mp4"|input video path
    "new_video_path"| "./videos/dsampled_video.mp4"|down-sampled video output path
    "new_video_width"| 800 | the width of the down-sampled video (same aspect ratio)
    "new_video_fps"| 5 | the new frame rate
     
* ## Helmet Detection Section
  Parameter|Value|Meaning
  ---------|-----|-------
  "output"| "./output/helmet_detection.avi"| the new video with rectangles around helmets
  "yolo"| "./yolo-coco" | the path to models weights
  "confidence"| 0.7 | only helmets with >70% confidence are shown 
  "threshold"| 0.3 | non-maxima suppression with threshold 30%
  
# 2. Run a Pre-trained DarkNet (YOLO)
This model (DarkNet) from OpenCV was trained on helmet detection. The GitHub repository adopted for this was https://github.com/AyazSaiyed/Helmet-Detection-.git (Many thanks to **Ayaz Saiyed** for the clear code). The weights for helmet detection were taken from this repository [https://github.com/BlcaKHat/yolov3-Helmet-Detection/blob/master/README.md](DarkNet_weights).

# 3. Containerise the Application
All previous steps were containerised using Docker, and an image with the name baselalyafi/python-helmet can be run.

# 4. How to Run?
Good question. To run this application please follow these steps:

    1. Run the command '<Docker run baselalyafi/python-helmet>'
    2. In case you want to try a different setting
        1. Locate the new video
        2. Create new_params.txt file following the description in section 1.
        3. '<docker run baselalyafi/python-helmet new_params.txt>'
    3. In case you need to run it without docker,
    you need to download the weights of the model as they
    are too large to be on GitHub.
          Steps:
            1. Go to https://drive.google.com/file/d/1953ngQ0bLa83Q2e3XGFHr6HAdFGvBrsf/view?usp=sharing
            2. Download into ./yolo-coco
            3. Creating a new environment is highly recommended before installing 
                the needed libraries using '<pip install -r requirements.txt>' 
            4. Run '<python3 ./helmet_detect.py params.txt>'
    4. In case you want only down-sampling (no helmet detection), 
    follow as before and check the 'videos' directory for the down-sampled 
    version of the video.

        
# 5. Example
This was the input video

https://user-images.githubusercontent.com/23275312/119231757-ca2a8b00-bb22-11eb-8044-c18f60ecf85a.mp4


And this was the ouput down-sampled and helmet detected with 0.6 confidence.

https://user-images.githubusercontent.com/23275312/119251469-00a9e980-bba7-11eb-8312-a8e67ad4a20b.mp4

Author: Basel Alyafi
https://baselalyafi.netlify.app/

Date: 23/05/2021
