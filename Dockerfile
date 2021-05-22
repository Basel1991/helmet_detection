#FROM ubuntu
#FROM python:slim-buster
#FROM python:3.6-alpine
#From alpine:latest
FROM python:3.6-slim-stretch

#--------------------------------------------------- alpine methods
#RUN apk add -q ffmpeg
#RUN apk add -q python3
#RUN apk add -q py3-pip
#RUN pip install --upgrade pip

#--------------------------------------------------
# RUN apt-get install -y --no-install-recommends wget xz-utils
# RUN apt-get -y upgrade
# RUN apt-get install -y python3
# RUN wget -q https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz && \

# tar xvf ffmpeg-git-amd64-static.tar.xz
 
# RUN mv ./ffmpeg-git-*/ffmpeg /usr/bin/ffmpeg

# RUN rm -rfd ./ffmpeg-git-*

# RUN rm -f ./ffmpeg-git-amd64-static.tar.xz

# RUN apt-get purge   --auto-remove
# RUN apt-get clean
#=============================================

COPY ./ /

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends ffmpeg
#RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y --no-install-recommends python3-pip
RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["python3", "./helmet_detect.py"]
CMD ["params.txt"]