import requests

import streamlit as st

styl = f"""
<style>
    .stChatFloatingInputContainer {{
      padding-bottom: 1rem;
    }}
    .block-container {{
      padding-top: 1rem;
    }}
</style>
"""

st.markdown(styl, unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, i'm your personall starlingX assitant. How can i help you?"}
    ]

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.chat_message(msg["role"], avatar="http://10.127.140.12:8080/static/themes/starlingx/img/favicon.png").write(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)


    with st.chat_message("assistant", avatar="http://10.127.140.12:8080/static/themes/starlingx/img/favicon.png"):
        response = requests.post("http://localhost:2000", json={"message": prompt}).text
        st.session_state.messages.append({"role": "assistant", "content": response, "avatar": "http://10.127.140.12:8080/static/themes/starlingx/img/favicon.png"})
        st.write(response)
