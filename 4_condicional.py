import streamlit as st
st.title ("Teste de Maior-idade")

idade = st.number_input("Digite a sua idade",min_value=0,max_value=130, step=1)

if st.button("verificar"):
    if idade < 18:
        st.write("Menor de idade")
    else:
        st.write("Maior de idade")

else:
    st.warning("Por favor, digite a idade.")