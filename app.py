import streamlit as st
import time

st.title("Study Technique Helper Bot")

# function to generate responses
# TODO: add logic to call utils/chatbot.py
def generate_response(prompt):
    # basic response for right now
    response = "Bot is thinking..."
    for word in response.split():
        yield word + " "
        time.sleep(0.08)

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you with your studies?"}]


# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# react to user input
if prompt := st.chat_input("Chat"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # st.markdown(response)
        response = st.write_stream(generate_response(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




