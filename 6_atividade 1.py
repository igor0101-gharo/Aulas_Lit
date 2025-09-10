import streamlit as st
st.title("Números e operações")

numero1 = st.number_input("Digite o primeiro número")
numero2 = st.number_input("Digite o segundo número")

maior = max(numero1,numero2)
menor = min(numero1,numero2)
media = (numero1+numero2)/2
soma = numero1+numero2
produto = numero1*numero2

if st.button("verificar"):
    st.info(f"Média:{media}")
    st.info(f"Soma:{soma}")
    st.info(f"Produto:{produto}")
    st.info(f"Maior valor:{maior}")
    st.info(f"Menor valor:{menor}")
else:
    st.warning("Aguardando números.")