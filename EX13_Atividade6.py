#Contar 5 números e dizer quais são pares e quais são ímpares
import streamlit as st
import time

st.title("Pares e ímpares - Atividade")
st.header("Laço de repetição - FOR")
st.write("Escreva um algoritmo que solicite ao usuário 5 valores inteiros e ao final mostre quantos números são pares e quantos são ímpares.")

pares = 0
impares = 0

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}º número.", step=1)
    resto = numero%2
    if resto == 0:
        pares = pares + 1
    else:
        impares = impares + 1

if st.button("Resultado"):
    st.info(f"Há {pares} número(s) par(es)")
    st.info(f"Há {impares} número(s) ímpar(es)")
else:
    st.warning("Por favor informe os números.")