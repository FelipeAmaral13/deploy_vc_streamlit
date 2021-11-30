FROM python:3.9

WORKDIR /opt
RUN apt update 
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN pip install --upgrade pip
RUN pip install numpy==1.21.0 \
				pandas==1.3.0 \
				scikit-learn==0.24.2 \
				matplotlib==3.4.2 \
				seaborn==0.11.1 \
				plotly==5.1.0 \
				streamlit==0.84.1

WORKDIR /work
