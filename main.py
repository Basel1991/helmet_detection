"""
This script is to run helmet detection and video downsampling code using ffmpeg.
Author: Basel Alyafi
22/05/2021
"""
import sys

from utils import down_sample
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # reading the parameters path. By default it's 'params.txt'
    if len(sys.argv) < 2:
        print("parameters file not passed, default is 'params.txt'")
        params_path = "params.txt"
    else:
        params_path = sys.argv[1]

    down_sample(params_path)
