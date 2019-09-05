FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip

COPY . /usr/local/src/image_controller/
WORKDIR /usr/local/src/image_controller/
RUN pip3 install -r /usr/local/src/image_controller/requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]
