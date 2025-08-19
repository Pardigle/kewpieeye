import streamlit as st
import pandas as pd
from functions import calculate_grades

st.title("Scuffed QPI Calculator")
st.divider()
st.subheader("Input your grades from AISIS and let the magic do its work.")

with st.form(key='main_qpi'):
    raw_grades = st.text_area("Grades from AISIS:")

    submit_button = st.form_submit_button("Submit")

    if submit_button and raw_grades:
        st.metric(label="QPI:", value=calculate_grades(raw_grades))
        st.balloons()