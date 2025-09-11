#Escrever um algoritmo para somar 5 números inteiros
import streamlit as st
import time
st.title("Soma de números Inteiros")
st.write("Escrever um programa de computador que solicite do usuário 5 números inteiros e, ao final, apresente a soma de todos os números lidos.")

st.warning("Digite 5 números.")
numero1 = st.number_input("número 1",step=1)
numero2 = st.number_input("número 2",step=1)
numero3 = st.number_input("número 3",step=1)
numero4 = st.number_input("número 4",step=1)
numero5 = st.number_input("número 5",step=1)
soma = numero1 + numero2 + numero3 + numero4 + numero5

if st.button("SOMAR"):
    st.info(f"A soma dos números é {soma}")
    st.success("FIM")