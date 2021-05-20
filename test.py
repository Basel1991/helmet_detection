import json

# read json file
import subprocess

with open("params.txt") as file:
    params = json.load(file)

video_path = params['video_path']
dsampled_path = params['new_video_path']

v_name = video_path
start = 0
out_w = 480
out_h = 360
x, y= 0, 0
width = 800
height = -2
end = 30
new_file = dsampled_path
new_fps = 5

command = f'ffmpeg -i {v_name} -ss {start}  -filter:v crop={out_w}:{out_h}:{x}:{y},scale={width}:{height}, fps={new_fps} -c:a copy -to {end} {new_file}'

subprocess.call(command, shell=True)
print(command)