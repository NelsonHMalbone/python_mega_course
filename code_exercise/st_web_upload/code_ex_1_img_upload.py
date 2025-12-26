import streamlit as st
from PIL import Image
import io

def download_photo():
    # convert img to bytes
    buf = io.BytesIO()
    convert_grayscale.save(buf, format="PNG")
    st.image(buf)

    st.download_button(label="Download Image",
                       data=buf.getvalue(),
                       file_name="gray_img.png",
                       mime="image/png")

st.title("Picture Upload Convertor")

with st.expander("start camera"):

    cam_to_be_taken = st.camera_input("Camera")

    if cam_to_be_taken is not None:
        open_im = Image.open(cam_to_be_taken)
        convert_grayscale = open_im.convert("L")
        download_photo()


with st.expander("upload a picture"):
    upload_photo = st.file_uploader("upload a picture")

    if upload_photo is not None:
        open_photo = Image.open(upload_photo)
        convert_grayscale = open_photo.convert("L")
        download_photo()