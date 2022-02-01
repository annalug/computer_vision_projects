
import streamlit as st
from utils import sketch,clean_folder
import numpy as np
from PIL import Image
import cv2 as cv


st.title('How would you like to make a sketch?')
option = st.selectbox(
     '',
     ('My webcam', 'Upload a photo'))

if option == 'My webcam':
    agree = st.checkbox('Start the cam!')
    if agree:
        picture = st.camera_input('')

        if picture:
            photo = np.array(Image.open(picture))
            col1, col2 = st.columns(2)

            with col1:
                st.write('Original photo')
                st.image((photo))
            with col2:
                st.write('Sketched photo')
                st.image(sketch(photo))

            cv.imwrite("photos/sketched_photo.png", sketch(photo))

            with open("photos/sketched_photo.png", "rb") as file:
                btn = st.download_button(
                    label="Download the sketch!",
                    data=file,
                    file_name="sketched_photo.png",
                    mime="image/png"
                )
            clean_folder('photos')
            st.write("Your photos aren't being saved anywhere!")

if option == 'Upload a photo':

    uploaded_file = st.file_uploader("Upload a photo!", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        uploaded_file = np.array(Image.open(uploaded_file))
         # our_image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.write('Original photo')
            st.image((uploaded_file))
        with col2:
            st.write('Sketched photo')
            st.image(sketch(uploaded_file))

        cv.imwrite("photos/sketched_photo.png", sketch(uploaded_file))

        with open("photos/sketched_photo.png", "rb") as file:
            btn = st.download_button(
                label="Download the sketch!",
                data=file,
                file_name="sketched_photo.png",
                mime="image/png"
            )
        clean_folder('photos')
        st.write("Your photos aren't being saved anywhere!")
