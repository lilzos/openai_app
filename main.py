import streamlit as st
import openai

# Initialize OpenAI client
client = openai.OpenAI(api_key="API-KEY")  # Replace with your actual key

# Streamlit page config
st.set_page_config(page_title="Simple Chatbot", page_icon="💬")

st.title("Chat with GPT")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:  # Skip the system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Say something..."):
    # Add user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=st.session_state.messages,
    )

    reply = response.choices[0].message.content

    # Add assistant's message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
