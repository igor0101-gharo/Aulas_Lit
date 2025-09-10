import streamlit as st
import time

st.title("Laço de repetição - FOR")

st.header("Contagem de 1 a 10")

if st.button("iniciar"):
    for i in range(1,11):
        st.info(i)
        time.sleep(1)
    st.header("FIM")
