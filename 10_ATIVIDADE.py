#Um algoritmo que mostrar a tabuada de um número escolhido
import streamlit as st
import time
st.title("Gerador de tabuada")
numero = st.number_input("Digite o número cuja tabuada você deseja", step=1)
escopo = st.number_input("Digite até qual número você quer a tabuada", step=1)

if st.button("tabuada"):
    for i in range(1,escopo+1):
        st.info(f"{numero} X {i}= {numero*i:.0f}")
        time.sleep(0.2)
    st.info("FIM")

