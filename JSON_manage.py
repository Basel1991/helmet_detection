import json

params = {}

params["video_path"] = "./video.mp4"
params["new_video_path"] = "./video_dsampled.mp4"
with open("params.txt", 'w') as file:
    json.dump(params, file, indent=5, sort_keys=False)