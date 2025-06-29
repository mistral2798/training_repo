import streamlit as st


# Введение возраста
age = st.number_input(label='Введите ваш возраст')
st.write(f'Вам {int(age)} лет')

#Изменение файла (Добавление новых строк)
name = st.text_input(label='Введите свое имя')
st.write('Ваше имя:', name)