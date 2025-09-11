#Algoritmo que escreve os números ímpares entre 1 e 20
import streamlit as st
import time
st.title("Números ímpares")
st.header("1 a 20")

if st.button("Iniciar"):
    for i in range(1,20,2):
        st.info(i)
        time.sleep(1)
        
    st.info("FIM")


     
