import streamlit as st

p = st.container()

tb = st.text_area("Question:")

if tb:
    p.write(tb)
