#receber 5 números e ver quantos são pares e quantos são ímpares.
import streamlit as st
import time
st.title("Pares e Ímpares")


numero1 = st.number_input("número 1",step=1)
numero2 = st.number_input("número 2",step=1)
numero3 = st.number_input("número 3",step=1)
numero4 = st.number_input("número 4",step=1)
numero5 = st.number_input("número 5",step=1)
resto1 = numero1%2
resto2 = numero2%2
resto3 = numero3%2
resto4 = numero4%2
resto5 = numero5%2
pares = 0
impares = 0

if resto1 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if resto2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if resto3 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if resto4 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if resto5 == 0:
    pares = pares + 1
else:
    impares = impares + 1

if st.button("RESULTADO"):
    st.info(f"Quantidade de números pares:{pares}")
    st.info(f"Quantidade de números ímpares:{impares}")