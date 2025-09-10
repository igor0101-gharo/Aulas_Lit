import streamlit as st
st.title("Verificando a média")

nota1 = st.number_input("Digite sua primeira nota.",max_value=10)
nota2 = st.number_input("Digite sua segunda nota.",max_value=10)

media = (nota1 + nota2)/2

if st.button("Verificar"):
    if media >= 7:
        st.success(f"Sua média foi {media}.Aprovado.")
    else:
        st.error(f"Sua média foi {media}.Reprovado.")
else:
    st.warning("Por favor informe suas notas.")

# sucess - verde
# warning - amarelo
# info - azul
# error - vermelho
