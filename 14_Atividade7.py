#Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.
import streamlit as st

st.title("Média de 4 Notas")
st.header("Laço de repetição- FOR")
st.write("Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.")

soma=0
for i in range(1,5):
    nota = st.number_input(f"Digite a {i}ª nota:", step = 0.1, max_value= 10)
    soma = soma + nota

media = soma/4

if st.button("Media"):
    st.info(f"Sua média é {media}")
else:
    st.warning("Informe suas notas.") 