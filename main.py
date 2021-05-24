"""
This script is to run helmet detection and video down-sampling code using ffmpeg.
Author: Basel Alyafi
Date: 22/05/2021
"""
import json
import sys
from utils import down_sample, post_request, detect_helmet

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # reading the parameters path. By default it's 'params.txt'
    if len(sys.argv) < 2:
        print("parameters file not passed, default is 'params.txt'")
        params_path = "params_win.txt"
    else:
        params_path = sys.argv[1]

with open(params_path) as file:
        params = json.load(file)
down_sample(params)

## this part is to push data to a mock web service
# no_helmets_data = detect_helmet(params)
# detect_helmet(params)
# url = 'enwgex0njtseq.x.pipedream.net'
# post_request(url, no_helmets_data)