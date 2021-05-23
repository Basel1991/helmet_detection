FROM python:3.6-slim-stretch
COPY ./ /

RUN apt-get -y update && \
apt-get install -y --no-install-recommends ffmpeg python3-pip && \
pip3 install -r ./requirements.txt && \
rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3", "./helmet_detect.py"]
CMD ["params.txt"]