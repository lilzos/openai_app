import streamlit as st
import openai
import pandas as pd
import os

client = openai.OpenAI(api_key="API-KEY")

# Load CSV data
tone_df = pd.read_csv("Tone_Comparisons.csv")

# Optionally filter or shorten the dataset for token length
csv_summary = tone_df.head(181).to_csv(index=False)

# System prompt with context description
system_message = f"""
You are an expert in analyzing media tone data.

You have access to a table that shows how different news outlet countries report on various themes (like economic or military),
in various action countries, involving various actors.

The key columns are:
- NewsOutletCountry: where the news outlet is based
- Theme: the topic of the reporting
- ActionCountry: where the event takes place
- Actor: the actor involved
- avg(Tone): the average sentiment tone

Here is the data you have access to:

{csv_summary}

Use this data to answer user questions thoughtfully.
"""

# Streamlit setup
st.set_page_config(page_title="ToneBot", page_icon="📊")
st.title("News Tone Analysis Chatbot")

# Store messages in session
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_message}]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask about news tone..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.chat.completions.create(
        model="ChatGPT-4o",
        messages=st.session_state.messages,
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
