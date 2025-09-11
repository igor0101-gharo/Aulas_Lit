#Algoritmo para contar de maneira decrescente de um número escolhido pelo usúario até 1
import streamlit as st
import time

st.title("Contador decrescente")
st.write("Escrever um algoritmo que solicite ao usuário um número e faça a contagem regressiva a partir do número informado até o número 1, aguardando um segundo para exibir cada número.")
numero = st.number_input("Digite o número inicial", min_value= 1, step= 1 )

if st.button("Contar"):
    for i in range(numero,0,-1):
        st.info(i)
        time.sleep(1)
    st.success("FIM")
    #st.snow()
    #st.balloons()