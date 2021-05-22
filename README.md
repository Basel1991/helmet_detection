# helmet_detection
Detecting helmets in a video using YOLO.

The steps that were followed to complete this task were as follows:

# 1. Video Downsampling
In this step, ffmpeg is used to scale (down or up) a given video. The parameters are all passed in the params.txt file (JSON format).

The default parameters' values are as follows:
  ## * "video_path": "./video.mp4"
  ## * "new_video_path": "./video_dsampled.mp4"
  ## * "new_video_width": 800
  ## * "new_video_fps": 5

The aspect ratio is kept the same whatever scaling is done.
  
# 2. Run a Pre-trained DarkNEt (YOLO)
# 3. Containerise the application
