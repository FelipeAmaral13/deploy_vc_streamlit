FROM python:3.9

WORKDIR /opt
RUN apt update 
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /work
