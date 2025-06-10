import streamlit as st
st.title("나의 첫 app")
st.write("Hello")
name=st.text_input("이름 입력")
if name:
  if name=="y/n":
    st.success("환영합니다.y/n!")
  else:
    st.warning("누구십니까?")
