import streamlit as st
import pandas as pd
import numpy as np

# Set title
st.title("🌐 Python Streamlit Website")

# Add a sidebar
st.sidebar.header("User Input")
name = st.sidebar.text_input("What is your name?")
age = st.sidebar.slider("Select your age", 1, 100, 25)

# Display user input
if name:
    st.success(f"Hello, {name}! 👋 You are {age} years old.")

# Add a chart
st.subheader("Random Chart Example")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

# Add a checkbox
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(chart_data)

# Add a button
if st.button("Click me"):
    st.balloons()
