import streamlit as st
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

api_key  = os.getenv("DEEPSEEK_API_KEY")  

# load system prompt
with open("./prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()
    
# init api client
client = OpenAI(api_key=api_key , base_url="https://api.deepseek.com")

st.set_page_config(
    page_title = "Study Assist UBC",
    page_icon = "🧠",
    layout="centered"
)

st.title("Study Assist UBC - Your Personal Study Assistant")
callout = st.container()
with callout:
    st.info("⭐ Refresh the page to get a new conversation! ⭐")


prompt = st.chat_input("Ask anything about school...")
    
    
if "chats" not in st.session_state:
    st.session_state.chats = []

if prompt:
    st.session_state.chats.append({
        "role": "user",
        "content": prompt
    })
    

    # generate response from api
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )
    
    st.session_state.chats.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })
    
for chat in st.session_state.chats:
    st.chat_message(chat["role"]).write(chat["content"])
    
    
