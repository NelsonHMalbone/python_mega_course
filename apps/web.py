import streamlit as st
import utils

lessons = utils.get_lesson()

def add_value_lesson():
    new_lesson = st.session_state["new_lessons"] + "\n"
    print(new_lesson)
    lessons.append(new_lesson)
    utils.write_lesson(lessons)


st.title("My Todo Web App")
st.write("This app is to increase productivity")

for lesson in lessons:
    st.checkbox(lesson)

st.text_input(label= "Enter a new lesson: ",
              on_change=add_value_lesson,
              key="new_lessons")