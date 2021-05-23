FROM python:3.6-slim-stretch
COPY ./ /
RUN apt-get -y update
RUN apt-get install -y --no-install-recommends ffmpeg
RUN apt-get install -y --no-install-recommends python3-pip
RUN pip3 install -r ./requirements.txt
ENTRYPOINT ["python3", "./helmet_detect.py"]
CMD ["params.txt"]