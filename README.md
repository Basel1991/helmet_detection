# helmet_detection
Detecting helmets in videos using YOLO v3.

The steps followed to complete this task were

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
This model (DarkNet) from OpenCV was trained on helmet detection. The GitHub repository adopted for this was [Helmet-Detection-](https://github.com/AyazSaiyed/Helmet-Detection-.git) (Many thanks to **Ayaz Saiyed** for the clear code). The weights for helmet detection were taken from this repository [DarkNet weights](https://github.com/BlcaKHat/yolov3-Helmet-Detection/blob/master/README.md).

# 3. Containerise the Application
All previous steps were containerised using Docker, and an image with the name baselalyafi/python-helmet can be run.

# 4. How to Run?
Good question. To run this application please follow these steps:

    1. Inside the same directory of docker-compose.yml, create a folder that contains
        a. 'videos' folder: contains the videos to work on
        b. 'output' folder: will contain the down-sampled versions and the final helmet detection
        c. params.txt modified accordingly
    2. add the created folder to docker-compose.yml volumes section and mount it to 'helmet'. e.g. if the folder named test:
        - test:/helmet
    3. Run the command '<docker-compose up>' when in the repository.
    4. In case you need to run it without docker, you need to download the weights of the model as they are too large to be on GitHub.
        Steps:
            1. Go to https://drive.google.com/file/d/1953ngQ0bLa83Q2e3XGFHr6HAdFGvBrsf/view?usp=sharing
            2. Download into ./yolo-coco
            3. Creating a new environment is highly recommended before installing 
                the needed libraries using '<pip install -r requirements.txt>' 
            4. Run '<python3 ./helmet_detect.py params.txt>'
    5. In case you want only down-sampling (no helmet detection), 
    follow as before and check the 'videos' directory for the down-sampled version of the video.

        
# 5. Example
This was the input video

https://user-images.githubusercontent.com/23275312/119231757-ca2a8b00-bb22-11eb-8044-c18f60ecf85a.mp4


And this was the ouput down-sampled and helmet detected with 0.6 confidence.

https://user-images.githubusercontent.com/23275312/119251469-00a9e980-bba7-11eb-8312-a8e67ad4a20b.mp4

Author: Basel Alyafi
https://baselalyafi.netlify.app/

Date: 23/05/2021
Last modified on 07/04/2022
