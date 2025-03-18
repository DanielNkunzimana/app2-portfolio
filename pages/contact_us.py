import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    row_message = st.text_area("your message")
    message = f"""\
Subject: New Email from {user_email}

from: {user_email}
{row_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("your email was sent successfully")