import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

option2=st.multiselect(
     'What is your favorite colors?',
     options=('Blue','Yellow','Green')
)
st.write('Your favorite colors are ', option2)

