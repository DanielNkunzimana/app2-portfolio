import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Daniel Nkunzimana")
    content = """
    Hi I'm Daniel Nkunzimana I am a python programmer and a student in BYU-Idaho. 
    I will be graduated within 2026 next year. I  am studying software development online degree program. 
    my goal is to become full stack software developer. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built. feel free to contact me!
"""
st.write(content2)