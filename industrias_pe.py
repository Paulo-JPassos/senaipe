# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import datetime as dt

# Título do dashboard
st.title("Indústrias de Pernambuco")

# Caminho do arquivo CSV na mesma pasta
csv_file = ("indupe.csv")

# Lê o arquivo CSV em um DataFrame (sem verificar se o arquivo existe)
df = pd.read_csv(csv_file, encoding='windows-1252', sep=';')

st.markdown("### Visão geral")

# Exibe os dados carregados
st.markdown("### Dados das indústrias de PE")
st.dataframe(df.head(10))

# Filtros de seleção
st.sidebar.header("Filtros")

# Filtro multiselect para "Porte da Empresa"
selected_porte = st.sidebar.multiselect(
    "Selecione o Porte da Empresa", 
    options=df['Porte da Empresa'].unique(),  # Exclui valores nulos se houver
    default=df['Porte da Empresa'].unique()
)

# Filtro multiselect para "Situação Cadastral"
selected_situacao = st.sidebar.multiselect(
    "Situação Cadastral", 
    options=df['Situação Cadastral'].dropna().unique(),
    default=df['Situação Cadastral'].dropna().unique()
)

# Aplicando os filtros no DataFrame
df_filtered = df[
    (df['Porte da Empresa'].isin(selected_porte)) &  # Filtra pelo porte da empresa
    (df['Situação Cadastral'].isin(selected_situacao))  # Filtra pela situação cadastral
]

# Exibindo o DataFrame filtrado
st.write("DataFrame filtrado:", df_filtered)
st.dataframe(df_filtered)  # Exibindo o DataFrame filtrado com formatação de tabela

# Gráfico de vendas por porte da empresa
st.markdown("### Gráfico de Porte da Empresa")
# Corrigido para utilizar o DataFrame filtrado corretamente
sales_by_porte = df_filtered.groupby('Porte da Empresa').size().sort_values(ascending=False)
st.bar_chart(sales_by_porte)

# Gráfico de vendas por situação cadastral
st.markdown("### Gráfico de Situação Cadastral")
# Corrigido para utilizar o DataFrame filtrado corretamente
sales_by_situacao = df_filtered.groupby('Situação Cadastral').size().sort_values(ascending=False)
st.bar_chart(sales_by_situacao)