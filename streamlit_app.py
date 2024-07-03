import streamlit as st
from datetime import time, datetime

st.header('st.select_slider')

# Example 1

#st.subheader('Slider')
color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
st.write("My favorite color is", color)

# Example 2

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"))
st.write("You selected wavelengths between", start_color, "and", end_color)



