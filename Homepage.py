import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Initialize session state
if "DeepSeek_API_Key" not in st.session_state:
    st.session_state["DeepSeek_API_Key"] = ""

if "Doubao_API_Key" not in st.session_state:
    st.session_state["Doubao_API_Key"] = ""

st.set_page_config(page_title="Welcome to LangChain of Python Classroom", layout="wide")

st.title("😄 Welcome to LangChain of Python Classroom")

# with st.container():
#     st.header("DeepSeek Settings")
#     st.markdown(f"""
#         | DeepSeek API Key |
#         | ---------------- |
#         | {st.session_state["DeepSeek_API_Key"]} |
#     """)

# with st.container():
#     st.header("Doubao Settings")
#     st.markdown(f"""
#         | Doubao API Key |
#         | ---------------- |
#         | {st.session_state["Doubao_API_Key"]} |
#     """)

# Chat interface
if st.session_state["DeepSeek_API_Key"]:
    with st.container():
        st.header("Chat with DeepSeek")
        prompt = st.text_input("Prompt", value="", max_chars=None, key=None, type="default")
        asked = st.button("Ask")
        if asked and prompt:
            try:
                chat = ChatOpenAI(
                    openai_api_key=st.session_state["DeepSeek_API_Key"],
                    openai_api_base="https://api.deepseek.com/v1",
                    model_name="deepseek-chat"
                )
                response = chat([HumanMessage(content=prompt)])
                st.success(f"Response: {response.content}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
elif st.session_state["Doubao_API_Key"]:
    with st.container():
        st.header("Chat with Doubao")
        prompt = st.text_input("Prompt", value="", max_chars=None, key="doubao_prompt", type="default")
        asked = st.button("Ask", key="doubao_ask")
        if asked and prompt:
            try:
                # Note: You'll need to configure the correct base URL and model for Doubao
                chat = ChatOpenAI(
                    openai_api_key=st.session_state["Doubao_API_Key"],
                    # openai_api_base="https://ark.cn-beijing.volces.com/api/v3",  # Update with correct URL
                    # model_name="doubao-pro-4k"  # Update with correct model name
                )
                response = chat([HumanMessage(content=prompt)])
                st.success(f"Response: {response.content}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
else:
    st.info("Please configure an API key in the settings pages to start chatting.")
