import json

params = {}

params["video_path"] = "E:\Python files\MGS_assignment\\v.mp4"
params["new_video_path"] = "E:\Python files\MGS_assignment\\v_dsampled.mp4"
with open("params.txt", 'w') as file:
    json.dump(params, file, indent=5, sort_keys=False)