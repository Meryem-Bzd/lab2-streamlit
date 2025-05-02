import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Streamlit Layouts and Containers Example')

# --- Layout with columns ---
st.header('Using Columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Column 1")
    st.button('Click me!')

with col2:
    st.subheader("Column 2")
    st.radio('Choose one:', ['Option 1', 'Option 2', 'Option 3'])

with col3:
    st.subheader("Column 3")
    st.selectbox('Select an item:', ['Apple', 'Banana', 'Cherry'])

# --- Container for grouping elements ---
st.header('Using a Container')

container = st.container()
container.write("This is inside a container.")

data = pd.DataFrame({
    'A': np.random.rand(5),
    'B': np.random.rand(5)
})
container.line_chart(data)

# --- Using an Expander for optional content ---
st.header('Using an Expander')

with st.expander("See more details"):
    st.write("""
        Here you can add extra information, explanations, or advanced options
        that the user can choose to view if they want.
    """)
    st.image('https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png', width=200)

# --- Streamlit Magic again ---
"This is a text displayed by Streamlit Magic."

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35]
})
df
