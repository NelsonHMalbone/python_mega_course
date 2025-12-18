import streamlit as st
from streamlit import session_state

import utils

lessons = utils.get_lesson()

def add_value_lesson():
    new_lesson = st.session_state["new_lessons"] + "\n"
    print(new_lesson)
    lessons.append(new_lesson)
    utils.write_lesson(lessons)
    st.session_state["new_lessons"] = ""

st.title("My Todo Web App")
st.write("This app is to increase productivity")
st.text_input(label= "Enter a new lesson: ",
              on_change=add_value_lesson,
              key="new_lessons"
              )

for index, lesson in enumerate(lessons):
    checkbox = st.checkbox(lesson, key=lesson)
    if checkbox:
        lessons.pop(index)
        utils.write_lesson(lessons)
        del st.session_state[lesson]
        st.rerun() # needed for checkboxes
