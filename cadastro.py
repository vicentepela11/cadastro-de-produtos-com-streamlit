import streamlit as st
import pydeck
import pandas as pd
import datetime
import base as b
import seaborn as sns
from matplotlib import pyplot as plt

import numpy as np
arr = np.random.normal(1, 1, size=100)



st.title("Cadatro de produtos")
teste = st.text_input("digite o nome do produto: ")
quant = st.number_input(f'qunatidade do produto {teste}: ', min_value=1)


diferenca = datetime.timedelta(hours=-3)
fuso = datetime.timezone(diferenca)
data_hora = datetime.datetime.now()


botao1 = st.button("finalizar")
if botao1:
    b.lista.append(teste)


    preco = (b.preco_venda[teste] * quant) - (b.dici[teste] * quant)
    b.lucro.append(preco)

    b.essencias['quantidade'].append(quant)
    b.essencias['produtos'].append(teste)
    b.essencias['lucro'].append(preco)

    lu = sum(b.essencias['lucro'])
    st.write(f"seu lucro foi de {lu}")

    tot = sum(b.lucro)
    b.total_dia['total'].append(tot)
    b.total_dia['data'].append(data_hora.astimezone(fuso).strftime("%H:%M"))

df = pd.DataFrame(b.essencias)
lucro_dia = pd.DataFrame(b.total_dia)

if st.sidebar.checkbox('tabela de dados'):
    st.dataframe(df)
    st.dataframe(lucro_dia)

if st.sidebar.checkbox('lucros do dia'):
    fig, ax = plt.subplots()
    ax.plot(lucro_dia['data'], lucro_dia['total'], marker='.', mew=1)
    st.pyplot(fig)

if st.sidebar.button("Salvar"):
    dia = datetime.date.today()
    df.to_csv(f'df_{dia.day}.{dia.month}.csv', index=False)
