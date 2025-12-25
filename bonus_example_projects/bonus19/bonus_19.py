import streamlit as st
from  PIL import Image
import io
# using streamlit creating a web app to take a picture and turn it to grayscale


st.title("Camera Web App")

cam_img = st.camera_input("camera")
print(cam_img)

if cam_img:
    # open cam image
    convert_img = Image.open(cam_img)
    # convert picture taken to a grayscale
    gray_img = convert_img.convert("L")
    # showing the img in a st image format to web page
    st.image(gray_img)

    # convert pil img to a bytes
    buf = io.BytesIO()
    gray_img.save(buf, format="PNG")
    byte_img = buf.getvalue()

    st.download_button(label="Download Image",
                       data=byte_img,
                        file_name="gray_img.png",
                        mime="image/png")
