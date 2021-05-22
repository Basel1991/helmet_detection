"""
This script is to write downsampling / YOLO running parameters to a JSON file ("params.txt")
"""
import json
params = {}

params["video_path"] = "./video.mp4"
params["new_video_path"] = "./video_dsampled.mp4"
params["new_video_width"] = 800
params["new_video_fps"] = 5

with open("params.txt", 'w') as file:
    json.dump(params, file, indent=5, sort_keys=False)