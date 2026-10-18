# COMO RODAR: python -m streamlit run sistema_venda.py
# (usar "python -m" porque a pasta Scripts não está no PATH)
# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos

# pip install streamlit pandas plotly
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

# Caminho do venda.csv, sempre na mesma pasta do sistema_venda.py
caminho_csv = Path(__file__).parent / "venda.csv"


tabela_vendas = pd.read_csv(caminho_csv)

# Carregar a base de vendas
# caminho_csv = mesma pasta do .py (funciona no deploy); index=False = não grava a numeração das linhas
tabela_vendas = pd.read_csv(caminho_csv, index=False)


st.write("# Sistema de Vendas")

#Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")

data = st.sidebar.date_input("Data da Venda")
produto = st.sidebar.text_input("Nome do Produto")
preco_unitario = st.sidebar.number_input("Preço Unitário",min_value=0.0)

quantidade = st.sidebar.number_input("Quantidade do Produto",step=1,min_value=0)

forma_pagamento = st.sidebar.selectbox("Forma de Pagamento",["PIX","dinheiro","Cartão de crédito","cartão de débito"])

botao_cadastrar = st.sidebar.button("Cadastrar Venda")

#logica de cadastro
if botao_cadastrar:

    if produto == "" or quantidade == 0 or preco_unitario == 0.0:
        st.warning("Venda com erros de preenchimento")
    else:
        nova_venda = [str(data),produto,preco_unitario,quantidade,forma_pagamento]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("venda.csv",index=False)
        st.success("Venda Cadastrada! com Sucesso")

#Seção de visualizar as vendas
st.write("# Vendas Cadastradas")
st.dataframe(tabela_vendas)
#Seção de Dashboard
st.write("## Dashboard")

# Card / Métrica -> Faturamento total
# Calcular o faturamento de cada venda
tabela_vendas["faturamento"] = tabela_vendas["preco_unitario"] * tabela_vendas["quantidade"]
faturamento = tabela_vendas["faturamento"].sum()
st.metric("Faturamento total",f"R$ {faturamento:.2f}")

# Gráfico de barras comparando o faturamento de diferentes produtos.


# Faturamento total por produto
faturamento_produto = tabela_vendas.groupby("produto")["faturamento"].sum().reset_index()

# Gráfico de barras
grafico = px.bar(faturamento_produto, x="produto", y="faturamento")
st.plotly_chart(grafico)