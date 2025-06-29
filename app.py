import streamlit as st
import pandas as pd

#Калькулятор ИМТ

st.title('Расчет ИМТ')

min_weight, max_weight = 40, 200
min_height, max_height = 100, 250

health_dir = {'выраженный дефицит массы тела':(0,16),
              'дефицит массы тела':(16,18.4),
              'норма':(18.5,24.9),
              'избыточная масса тела (предожирение)':(25,29.9),
              'ожирение первой степени':(30,34.9),
              'ожирение второй степени':(35,39.9),
              'ожирение третьей степени (морбидное)':(40,1000)}

weight, height = st.columns(2,border=True)

with weight:
    weight = st.number_input(label='Вес, кг', min_value=min_weight, max_value=max_weight)

with height:
    height = st.number_input(label='Рост, см', min_value=min_height, max_value=max_height)

IMT = weight / (height/100)**2

IMT_round = round(IMT, 1)
st.metric('Ваше значение ИМТ составляет: ', IMT_round)

highlight_index = 0
for k, (low,high) in health_dir.items():
    highlight_index += 1
    if low <= IMT_round <= high:
        st.write('У вас', k)
        break

url_web_table = 'https://ria.ru/20220514/ves-1788536975.html'
tables = pd.read_html(url_web_table)
df = tables[0][1:]
df.columns = ['Диапазон ИМТ', 'Результат']

def highlight_row(row):
    if row.name == highlight_index:
        return ['background-color: lightgreen'] * len(row)
    else:
        return [''] * len(row)

styled_df = df.style.apply(highlight_row, axis=1)
st.dataframe(styled_df, hide_index=True)

