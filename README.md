# helmet_detection
Detecting helmets in a video using YOLO.

The steps that were followed to complete this task were as follows:

# 1. Video Downsampling
In this step, ffmpeg is used to scale (down or up) a given video. The parameters are all passed in the params.txt file (JSON format).

Examples of the parameters' values are given below:
 * ## Video down-sampling section
   Parameter|Value|Meaning
   ---------|-----|-------
    "video_path"| "./videos/video.mp4"|input video path
    "new_video_path"| "./videos/dsampled_video.mp4"|down-sampled video output path
    "new_video_width"| 800 | the width of the down-sampled video (same aspect ration)
    "new_video_fps"| 5 | the new frame rate
     
* ## Helmet detection section
  Parameter|Value|Meaning
  ---------|-----|-------
  "output"| "./output/helmet_detection.avi"| the new video with rectangles around helmets
  "yolo"| "./yolo-coco" | the path to models weights,
  "confidence"| 0.7 | only helmets with >70% confidence are shown 
  "threshold"| 0.3 | non-maxima suppression with threshold 30%
  
# 2. Run a Pre-trained DarkNEt (YOLO)
This model (darknet) from opencv was trained on helmet detection. The github reposirtory adopted for this was https://github.com/AyazSaiyed/Helmet-Detection-.git (Many thanks to **Ayaz Saiyed** for the clear code).

# 3. Containerise the application
All previous steps were containerised using docker and an image with the name baselalyafi/python-helmet can be run.

# 4. How to run?
Good question. To run this application please follow these steps:

    1. Run the command '<Docker run baselalyafi/python-helmet>'
    2. In case, you want to try a different setting
        1. Download the video
        2. create new_params.txt file following the description in section 1.
        3. '<docker run baselalyafi/python-helmet new_params.txt>'
    3. In case you want only down-sampling (no helmet detection), follow as before and check the videos directory for the dsampled version of the video.
        
