"""
Author: Basel Alyafi
Date: 23/05/2021
"""
import json
import subprocess

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