# main.py

import cv2
import streamlit as st
import numpy as np
import os

def main():

    selected_box = st.sidebar.selectbox(
    'Escolha as seguintes opções',
    ('Welcome','Segmentar cor', 'Detectar Face', 'Cartoon')
    )

    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Segmentar cor':
        seg_color()
    if selected_box == 'Cartoon':
        cartoon()

def welcome():
    
    st.title('Deploy de uma sistema de Visão Computacional')
    
    st.subheader('Um simples deploy de um sistema de visão Computacional'\
                 ' utilizando Python e Streamlit.')
    st.write(' Escolha no menu Lateral qual ferramenta usar:')
    st.write('1) Welcome')
    st.write('2) Segmentar Cor')
    st.write('3) Cartoon')


def seg_color():

    st.title("Webcam Segementation Color")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    cam = cv2.VideoCapture(0)       

    while run:        
        ret, frame = cam.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)               

        # Mascara
        lower_blue = np.array([100, 120, 80])
        upper_blue = np.array([255, 255, 255])
        # Aplicando a mascara
        mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        frame_RGB = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

        FRAME_WINDOW.image(frame_RGB)
    else:
        st.write('Sem Acesso a Camera')



def cartoon():
    st.title("Cartoon")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    cam = cv2.VideoCapture(0)       

    while run:        
        ret, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)               

        # Edges
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # Cartoon
        color = cv2.bilateralFilter(frame, 9, 250, 250)
        carton = cv2.bitwise_and(color, color, mask=edges)

        FRAME_WINDOW.image(carton)
    else:
        st.write('Sem Acesso a Camera')


if __name__ == "__main__":
    main()