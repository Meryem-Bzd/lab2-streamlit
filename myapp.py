import streamlit as st
import pandas as pd

# Display widgets
st.title('Test Streamlit Widgets')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a simple text')
st.markdown('**This is a bold text with Markdown**')
st.code('print("Hello Streamlit")', language='python')

# Input widgets
name = st.text_input('Enter your name')
message = st.text_area('Enter a message')
age = st.number_input('Enter your age', min_value=0, max_value=100)
birthday = st.date_input('Select your birthday')
appointment = st.time_input('Select a time')

# File widget
uploaded_file = st.file_uploader("Upload a file")

# Filters widgets
like_streamlit = st.checkbox('Do you like Streamlit?')
favorite_color = st.radio('Choose your favorite color', ['Red', 'Green', 'Blue'])
hobby = st.selectbox('Choose a hobby', ['Reading', 'Traveling', 'Cooking'])
skills = st.multiselect('Select your skills', ['Python', 'Machine Learning', 'Data Analysis'])
satisfaction = st.slider('Rate your satisfaction', 0, 10, 5)
level = st.select_slider('Select your level', options=['Beginner', 'Intermediate', 'Advanced'])

# Button widgets
if st.button('Click me'):
    st.success('Button clicked!')

st.download_button('Download Text', 'Hello World!', file_name='hello.txt')

# Data widgets
data = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})
st.dataframe(data)
st.table(data)

# Other widgets
color = st.color_picker('Pick a color')
st.write(f'You picked {color}')
