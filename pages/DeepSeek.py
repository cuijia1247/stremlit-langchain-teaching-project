import streamlit as st

if "DeepSeek_API_Key" not in st.session_state:
    st.session_state["DeepSeek_API_Key"] = ""


st.set_page_config(page_title="DeepSeek Settings", layout="wide")

st.title("DeepSeek Settings")

deepseek_api_key = st.text_input("API Key", value=st.session_state["DeepSeek_API_Key"], max_chars=None, key=None, type="default")

saved = st.button("Save")

if saved:
    st.session_state["DeepSeek_API_Key"] = deepseek_api_key