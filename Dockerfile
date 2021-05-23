FROM python:3.6-slim-stretch
COPY ./ /
RUN apt-get -y update
RUN apt-get install -y --no-install-recommends ffmpeg
RUN apt-get install -y --no-install-recommends python3-pip
RUN pip3 install -r ./requirements.txt
RUN apt-get -y --no-install-recommends wget
RUN wget -O yolov3-obj_2400.weights https://drive.google.com/uc?id=1DHB9BM00df9P35pT9WkWyCldwMOzHjuc&export=download
RUN mv /yolov3-obj_2400.weights /yolo-coco
ENTRYPOINT ["python3", "./helmet_detect.py"]
CMD ["params.txt"]