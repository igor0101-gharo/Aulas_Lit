import streamlit as st
st.title("Login e Senha")
st.write("Crie um programa que solicite ao usuário seu login e uma senha.")
st.write("O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")
st.write("O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

login_salvo = "coxinha"
senha_salva = "quibe"

login = st.text_input("Login")
senha = st.text_input("Senha",type= "password")
if "tentativas" not in st.session_state:
       st.session_state.tentativas = 0

if st.button ("verificar"):
    if st.session_state.tentativas == 3:
           st.info("Número de tentativas esgotado")
    elif login == login_salvo and senha == senha_salva:
            st.success("Bem-vindo")
    else:
            st.error("Login ou Senha incorretos.")
            st.session_state.tentativas +=1
