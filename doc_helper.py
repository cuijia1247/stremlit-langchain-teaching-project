"""
文档助手工具 - 用于显示函数文档
"""
import streamlit as st
import inspect

def show_function_docs(func):
    """显示函数的文档字符串和签名"""
    print(f"Function: {func.__name__}")
    print(f"Signature: {inspect.signature(func)}")
    print(f"Documentation:\n{inspect.getdoc(func)}")
    print("-" * 50)

if __name__ == "__main__":
    # 示例：显示st.button的文档
    show_function_docs(st.button)
    show_function_docs(st.write)
    show_function_docs(st.selectbox)
