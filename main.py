import openai
import streamlit as st

openai.api_key = "sk-insert Your OpenAI API Key" 

st.set_page_config(page_title="CatGPT", page_icon=":speech_balloon:")

st.title("CatGPT like Chatbot")
st.write("Meow Meow Meow Meow Meow Meow I am a CyberCat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Meow Meow?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call OpenAI's chat API (no Assistant needed)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cat. Respond mostly with MEOWs. Only 4 English words allowed per message."},
            *st.session_state.messages,
        ]
    )

    reply = response.choices[0].message["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
