import streamlit as st
import time

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")


if st.button("Login"):

    if username == "amangupta@gmail.com" and password == "12345":
        st.success("Login successful!")
        st.success('This is a success message!', icon="✅")

    else:
        st.error("Invalid username or password")
