import streamlit as st
st.title("My first app!")

name = st.text_input("hey whats ur name?")
if name:
  st.write9/f"hello, {name}!")
