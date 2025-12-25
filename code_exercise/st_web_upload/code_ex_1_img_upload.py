import streamlit as st
from PIL import Image
import io


st.title("Picture Upload Convertor")

with st.expander("start camera"):

    cam_to_be_taken = st.camera_input("Camera")

    if cam_to_be_taken:
        open_im = Image.open(cam_to_be_taken)
        convert_grayscale = open_im.convert("L")
        st.image(convert_grayscale)

        # convert img to bytes
        buf = io.BytesIO()
        convert_grayscale.save(buf, format="PNG")
        st.image(buf)

        st.download_button(label="Download Image",
                           data=buf.getvalue(),
                           file_name="gray_img.png",
                           mime="image/png")

st.expander("upload a picture")
