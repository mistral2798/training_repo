import streamlit as st

st.write('# To-Do app')

if "task" not in st.session_state:
    st.session_state['task'] = []

with st.form(key='add_form', clear_on_submit=True): # Создание формы с ключом добавления формы
    new_task = st.text_input("Введите задачу:") # Поле ввода текста
    submitted = st.form_submit_button("Добавить") # Кнопка отправки формы
    if submitted and new_task: # Если введен текст и отправлена форма
        st.session_state.task.append({'text': new_task, 'done':False}) # То добавляем в список задач словарь из двух пар (задача: описание, выполнение: Да/Нет)

"---"
st.write('### Ваш список задач:')

for i, dct in enumerate(st.session_state.task): # Проходимся по индексам и словарям в списке задач
    checked = st.checkbox(dct['text']) # Чекбокс с текстом задачи
    st.session_state.task[i]['done'] = checked # Запись значения чекбокса в ключ выполнения

if st.button("Удалить выполненные задачи"):
    st.session_state.task = [t for t in st.session_state.task if not t['done']]