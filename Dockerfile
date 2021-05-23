FROM python:3.6-slim-stretch
COPY ./ /

RUN apt-get -y update && \
apt-get install -y --no-install-recommends ffmpeg python3-pip wget

RUN pip3 install -r ./requirements.txt

RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1953ngQ0bLa83Q2e3XGFHr6HAdFGvBrsf' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1953ngQ0bLa83Q2e3XGFHr6HAdFGvBrsf" -O yolov3-obj_2400.weights.tar.gz && rm -rf /tmp/cookies.txt

RUN tar xf yolov3-obj_2400.weights.tar.gz && \
rm yolov3-obj_2400.weights.tar.gz && \
rm -rf /var/lib/apt/lists/* && \
ls && \
mv yolov3-obj_2400.weights yolo-coco/

ENTRYPOINT ["python3", "./helmet_detect.py"]
CMD ["params.txt"]