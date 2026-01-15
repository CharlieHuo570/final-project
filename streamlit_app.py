import streamlit as st

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

number = 0

clicked_button = st.button("Press me!")
if clicked_button:
    number += 1

st.write(number)