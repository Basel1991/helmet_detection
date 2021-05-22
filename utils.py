import json
import subprocess

def down_sample(json_path):
    """
    This function downsamples a video (given the video_path in the passed JSON file)
    It sets the fps (frames per second) to five by default.
    :param file_path: str, the path to the JSON parameters file
    :return: void
    """
    with open(json_path) as file:
        params = json.load(file)

    # read the path to the video and the path where to save the down-sampled version
    video_path = params['video_path']
    dsampled_path = params['new_video_path']
    width = params['new_video_width']

    # this height is to keep the same aspect ratio
    height = -2
    new_fps = params['new_video_fps']

    command = f'ffmpeg -i "{video_path}" -r {new_fps}  -filter:v scale={width}:{height} "{dsampled_path}"'

    subprocess.call(command, shell=True)
    print(command)