# frontend.py

# Import necessary libraries
import streamlit as st  # For building the frontend interface
import requests         # For making HTTP requests to the FastAPI backend

# Configure the page layout and title
st.set_page_config(page_title="Gemini Chatbot", layout="centered")

# Page title
st.title("Gemini Chatbot")
st.markdown("Ask me anything!")

# --- User Input Section ---
# Capture user input from a text input box
user_input = st.text_input("You:", key="user_input")

# If user has entered a prompt, send it to the backend and display response
if user_input:
    with st.spinner("Thinking..."):
        try:
            # Send POST request to FastAPI backend
            response = requests.post("http://127.0.0.1:8000/chat", json={"input": user_input})
            
            # Display response if request was successful
            if response.ok:
                st.markdown("**Bot:** " + response.json()["response"])
            else:
                st.error("Failed to get response from backend.")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Is it running?")

# --- Creative Use Case: Mental Fitness Prompt ---
st.markdown("---")
st.subheader("Mental Fitness Prompt")

# Example mental health-related prompt
example_prompt = "I'm feeling overwhelmed with work lately."

# Button to trigger a pre-defined mental health prompt
if st.button("Try Mental Health Prompt"):
    with st.spinner("Thinking like a coach..."):
        try:
            response = requests.post("http://127.0.0.1:8000/chat", json={"input": example_prompt})
            
            if response.ok:
                # Display both user and bot messages
                st.markdown("**You:** " + example_prompt)
                st.markdown("**Bot:** " + response.json()["response"])
            else:
                st.error("Failed to get response from backend.")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Is it running?")
