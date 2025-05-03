# main file for front end 
import streamlit as st

st.title("Streamlit Basic Frontend")
st.write("We need to conceptualize ideas!")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
