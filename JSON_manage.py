"""
This script is to write downsampling / YOLO running parameters to a JSON file ("params.txt")

Author: Basel Alyafi
Date: 23/05/2021
"""
import json
params = {}

#-------------- video down-sampling section
#-------------- check https://github.com/Basel1991/helmet_detection for details.

params["video_path"] = "./videos/video.mp4"
params["new_video_path"] = "./videos/video_dsampled.mp4"
params["new_video_width"] = 800
params["new_video_fps"] = 5

#-------------- helmet detection section
params["output"] = "./output/helmet_detection.avi"
params["yolo"] = "./yolo-coco"
params["confidence"] = 0.6
params["threshold"] = 0.3

with open("params.txt", 'w') as file:
    json.dump(params, file, indent=5, sort_keys=False)