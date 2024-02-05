import os

import requests
import streamlit as st

styl = f"""
<style>
    .stChatFloatingInputContainer {{
      padding-bottom: 1rem;
    }}
    .block-container {{
      padding-top: 2rem;
    }}
</style>
"""

st.markdown(styl, unsafe_allow_html=True)


def submit(model, temperature, host_ip):
    headers = {'temperature': str(temperature), 'model': model}
    session_api = f'http://{host_ip}:2000/session'
    st.session_state["session_id"] = requests.get(session_api, headers=headers).text
    st.session_state["step"] = "chat"


host_ip = os.environ['HOST_IP']

if "step" not in st.session_state:
    st.session_state["step"] = "create_session"

if st.session_state.step == "create_session":
    st.write("Enter your session details")
    model = st.selectbox(
        'Which model do you want to use?',
        ('gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo-preview'))
    temperature = st.slider("Model temperature", min_value=0.0, max_value=2.0, value=0.5)
    st.button("Let's go!", on_click=submit, args=[model, temperature, host_ip])

if st.session_state.step == "chat":
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hi, I'm your personal StarlingX assistant. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"],
                            avatar=f"http://{host_ip}:8080/static/themes/starlingx/img/favicon.png").write(
                msg["content"])
        else:
            st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant", avatar=f"http://{host_ip}:8080/static/themes/starlingx/img/favicon.png"):
            response = requests.post(f"http://{host_ip}:2000/chat",
                                     json={"message": prompt, "session_id": st.session_state.session_id}).text
            st.session_state.messages.append({"role": "assistant", "content": response,
                                              "avatar": f"http://{host_ip}:8080/static/themes/starlingx/img/favicon.png"})
            st.write(response)
