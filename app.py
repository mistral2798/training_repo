import streamlit as st


# Введение возраста
age = st.number_input(label='Введите ваш возраст')
st.write(f'Вам {int(age)} лет')