FROM python:3.8

EXPOSE 8501

RUN apt update 
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

RUN pip3 install -r requirements.txt

CMD streamlit run app.py
