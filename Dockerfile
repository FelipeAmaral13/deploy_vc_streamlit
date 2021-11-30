FROM python:3.8

EXPOSE 8501

RUN apt update 
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD streamlit run app.py
