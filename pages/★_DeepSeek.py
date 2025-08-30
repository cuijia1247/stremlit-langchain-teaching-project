import streamlit as st

if "DeepSeek_API_Key" not in st.session_state:
    st.session_state["DeepSeek_API_Key"] = ""


st.set_page_config(page_title="DeepSeek Settings", layout="wide")

st.title("DeepSeek Settings")

deepseek_api_key = st.text_input("API Key", value=st.session_state["DeepSeek_API_Key"], max_chars=None, key=None, type="password")

saved = st.button("Save")

if saved:
    st.session_state["DeepSeek_API_Key"] = deepseek_api_key
    st.success("DeepSeek API Key 已保存成功！")
    st.info(f"当前保存的 API Key: {deepseek_api_key[:8]}..." if deepseek_api_key else "当前保存的 API Key: 未设置")

# 显示当前状态
st.markdown("---")
st.subheader("当前配置状态")
if st.session_state["DeepSeek_API_Key"]:
    st.success("✅ DeepSeek API Key 已配置")
    # 显示部分API Key用于确认（隐藏敏感信息）
    masked_key = st.session_state["DeepSeek_API_Key"][:8] + "*" * (len(st.session_state["DeepSeek_API_Key"]) - 8) if len(st.session_state["DeepSeek_API_Key"]) > 8 else st.session_state["DeepSeek_API_Key"]
    st.text(f"API Key: {masked_key}")
else:
    st.warning("⚠️ DeepSeek API Key 未配置")

# 清除API Key功能
st.markdown("---")
if st.button("清除 API Key", type="secondary"):
    st.session_state["DeepSeek_API_Key"] = ""
    st.success("DeepSeek API Key 已清除")
    st.rerun()

# 帮助信息
st.markdown("---")
st.subheader("📚 帮助信息")
st.markdown("""
### 如何获取DeepSeek API Key:
1. 访问 [DeepSeek官网](https://platform.deepseek.com/)
2. 注册并登录账户
3. 进入控制台，创建应用
4. 获取 API Key 并复制到上方输入框
5. 点击保存按钮

### 使用说明:
- API Key 将保存在当前会话中
- 重新启动应用后需要重新配置
- API Key 显示时会自动隐藏敏感信息
""")