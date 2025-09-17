import streamlit as st
st.title("Login e Senha")
st.write("Um algoritmo que pede login e senha do usuário e avisa quando incorreto")

login = "coxinha123"
senha = "quibe456"

uselogin = st.text_input("Digite seu Login")
usesenha = st.text_input("Digite sua Senha", type="password")

if st.button("Logar"):
    if uselogin == login and usesenha == senha:
        st.success("Você está logado!")
    else:
        st.error("Login ou Senha incorreta. Tente novamente")