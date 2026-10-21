# Sistema de Vendas - Gcell

Protótipo de um Sistema de Vendas para a **Gcell**, loja real de produtos eletrônicos e acessórios para celulares, localizada em Teresina-PI.

## Sobre o projeto

O projeto consiste no desenvolvimento de um protótipo baseado nas necessidades reais de um vendedor da loja, permitindo registrar vendas, consultar informações e visualizar gráficos que auxiliem no acompanhamento dos resultados comerciais.

## Objetivos

- Desenvolver uma solução baseada nas necessidades reais de um vendedor da loja.
- Permitir o registro de vendas, a consulta das informações e a visualização de gráficos.
- Validar o protótipo em um cenário real de uso, considerando a rotina do vendedor, suas dificuldades e suas sugestões de melhoria.

## Funcionalidades

- Cadastro de vendas (data, produto, preço unitário, quantidade e forma de pagamento) com validação dos campos.
- Armazenamento das vendas em arquivo CSV.
- Tabela com todas as vendas cadastradas.
- Dashboard com o faturamento total e gráfico de barras do faturamento por produto.

## Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

## Como executar

1. Clone o repositório e entre na pasta do projeto.
2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o sistema:

```
python -m streamlit run sistema_venda.py
```

4. Acesse `http://localhost:8501` no navegador.

## Como parar e executar novamente

Para encerrar o sistema, volte ao terminal onde o Streamlit está rodando e pressione **Ctrl+C**. Se não parar na primeira vez, pressione novamente. Depois disso, o endereço `http://localhost:8501` deixa de funcionar no navegador.

Para executar novamente, use o mesmo comando:

```
python -m streamlit run sistema_venda.py
```

> Se você alterar o código com o sistema aberto, não é preciso reiniciar: o Streamlit detecta a mudança e mostra no navegador a opção **Rerun** (ou **Always rerun**) para atualizar a página.

## Estrutura do projeto

```
├── sistema_venda.py   # código do sistema
├── venda.csv          # base de vendas (dados fictícios)
├── requirements.txt   # dependências
└── README.md
```

## Minha participação

- **Desenvolvi** o protótipo completo do sistema de vendas, da tela de cadastro ao dashboard.
- **Fui responsável** por levantar as necessidades do vendedor, projetar as telas, implementar o cadastro com validação, o salvamento dos dados e os gráficos.
- **Utilizei** Python, Streamlit, Pandas e Plotly.
- **Obtivemos o resultado:** o protótipo foi validado com um vendedor real da loja, usando apenas dados fictícios. No questionário de avaliação (Google Forms), ele atribuiu nota máxima (5/5) para a facilidade de uso no cadastro de vendas, para a rapidez e praticidade do formulário e para a utilidade do dashboard no acompanhamento das vendas. O feedback também indicou melhorias para uma próxima versão: função para apagar uma venda em caso de troca ou devolução e cálculo automático da quantidade de itens repetidos na mesma compra.

## Aviso sobre os dados

O teste é gratuito e utiliza **exclusivamente dados fictícios**, preservando as informações reais e confidenciais da empresa.

**Segurança de Dados:** Garanti a conformidade e a segurança da informação utilizando **dados fictícios** mascarados para testes de usabilidade, preservando o sigilo comercial da empresa.