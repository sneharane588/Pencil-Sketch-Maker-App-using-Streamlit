import streamlit as st
import numpy as np
from PIL import Image # used for image manipulation
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)

def pencilsketch(input_img):
    img_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray) # for negative effect by inverting the img
    img_blur = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_blur)
    return(final_img)

st.title('Pencil Sketch App')
st.write('Now you can easily convert your pics to realistic sketches...')

file_img = st.sidebar.file_uploader("Upload your Images", type=['jpeg', 'png', 'jpg'])

if file_img is None:
    st.write("You haven't uploaded any image file")
else:
    input_img = Image.open(file_img)
    final_sketch = pencilsketch(np.array(input_img))
    st.write("**  INPUT PHOTO  **")
    st.image(file_img, use_column_width=True)
    st.write("**  OUTPUT SKETCHED PHOTO  **")
    st.image(final_sketch, use_column_width=True)

st.write('made by Sneha Rane')
