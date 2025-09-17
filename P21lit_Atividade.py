import streamlit as st
st.title("Login e Senha")
st.write("Crie um programa que solicite ao usuário seu login e uma senha.")
st.write("O programa deve continuar pedindo o login e a senha até que ambos estejam corretos.")
st.write("O programa deve solicitar o login e senha apenas três vezes. Caso ultrapasse o número de tentativas, o programa deve ser finalizado.")

login_salvo = "coxinha"
senha_salva = "quibe"
st.session_state.setdefault("desabilitar", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("Login", disabled=st.session_state.desabilitar)
senha = st.text_input("Senha",type= "password", disabled=st.session_state.desabilitar)


if st.button ("verificar"):
    if login == login_salvo and senha == senha_salva:
            st.success("Bem-vindo")
    else:
              st.session_state.tentativas += 1
              if st.session_state.tentativas < 3:
                   st.error(f"Login ou Senha incorretos.{st.session_state.tentativas}")
              else:
                     st.error(f"Login ou Senha incorretos.{st.session_state.tentativas}")
                     st.session_state.desabilitar = True
              
       
