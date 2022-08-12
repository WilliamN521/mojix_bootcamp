import streamlit as st

list_input = st.text_input("List")
st.write(f"You enter a {list_input}")