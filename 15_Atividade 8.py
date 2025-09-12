import streamlit as st
st.title("Notas e média")
st.header("Atividade laço de repetição - FOR")
st.write("Escrever um programa de computador que solicite do usuário 3 notas e, ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. ")
st.write("Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.")

soma = 0
for i in range (1,4):
    nota = st.number_input(f"Digite a {i}ª Nota.", step = 0.1, max_value= 10.00)
    soma = soma + nota

media = soma/3

if st.button("Resultado"):
    if media >= 7:
        st.success(f"Você está aprovado. Sua média foi {media}")
    elif media < 7 and media >= 4:
        st.info(f"Você está de recuperação. Sua média foi {media}")
    elif media < 4:
        st.error(f"Você está reprovado. Sua média foi {media}")
else:
    st.warning("Informe suas notas.")

