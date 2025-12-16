import streamlit as st
import utils

lessons = utils.get_lesson()

st.title("My Todo Web App")
st.write("This app is to increase productivity")

for lesson in lessons:
    st.checkbox(lesson)

st.text_input(label= "Enter a new lesson: ")