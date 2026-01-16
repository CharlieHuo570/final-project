import streamlit as st

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""
if 'number' not in st.session_state:
    st.session_state['number'] = 0

clicked_button = st.button("Press me!")
if clicked_button:
    st.session_state['number']  += 1

st.write(st.session_state['number'] )