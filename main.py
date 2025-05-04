# app.py

import streamlit as st
from ai import generate_prompt

st.title("🔍 AI Web Scraper Prompt Generator")

# Input from the user
user_query = st.text_input("Enter your query:", "")

# When user hits submit
if st.button("Submit"):
    if user_query:
        with st.spinner("Generating prompts..."):
            try:
                prompts = generate_prompt(user_query)
                st.subheader("Generated Prompts:")
                for p in prompts:
                    st.write(f"- {p}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query before submitting.")
user_query2 = st.text_input("What would you like to do with this web-scraped information?")
if st.button("Do it!"):
    if user_query2:
        with st.spinner("Ok ! Now doing.."):
            try:
                st.write("This is a placeholder for now. but ideally we would use the query and the previous data, send it to ai then save it in a variable ")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query before submitting.")