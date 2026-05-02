import streamlit as st
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "..", "src")
sys.path.append(src_path)

from predict import predict

st.title("Sentiment Analyzer")

user_input = st.text_input("Enter text: ")

if st.button("Predict"):
    if user_input:
        result = predict(user_input)
        st.write("AI result: ", result)
    else:
        st.write("Please write some text")