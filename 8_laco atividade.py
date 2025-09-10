import streamlit as st
st.title("Números pares")
st.header("100 a 120")

if st.button("Contar"):
    for i in range(100,121,2):
        st.write(i)