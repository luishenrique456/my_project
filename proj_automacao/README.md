# 🤖 Automação de Cadastro de Produtos com Python

Projeto de automação de tarefas repetitivas usando **PyAutoGUI** e **Pandas**, desenvolvido com base no conteúdo do canal **Hashtag Treinamentos** (YouTube). O objetivo é entrar em um sistema, fazer login e cadastrar automaticamente uma lista de produtos lida de um arquivo CSV.

> ⚠️ **Projeto de estudo:** foi utilizado um site de testes e um arquivo `produtos.csv` de exemplo, disponibilizados pelo curso. Nenhum sistema ou dado real de empresa foi utilizado.

---

## 📌 Sobre o projeto

Em muitas empresas, cadastrar produtos manualmente em um sistema é uma tarefa lenta, repetitiva e sujeita a erros de digitação. Este projeto simula esse cenário e mostra como o Python pode executar todo o processo sozinho.

**O que eu fiz:**

- **Desenvolvi** um script em Python que automatiza todo o fluxo de cadastro de produtos em um sistema web de testes.
- **Fui responsável** por toda a implementação: abrir o navegador, acessar o sistema, fazer login, ler a base de dados e preencher o formulário para cada produto.
- **Utilizei** a biblioteca **PyAutoGUI** para simular cliques, digitação e atalhos de teclado, e a biblioteca **Pandas** para ler e percorrer a base de dados `produtos.csv`.
- **Obtive como resultado** um processo totalmente automatizado: o script cadastra todos os produtos da lista, um após o outro, sem intervenção manual, eliminando o trabalho repetitivo e reduzindo o risco de erros de digitação.

---

## ⚙️ Como funciona (passo a passo)

1. **Entrar no sistema:** abre o Chrome pelo menu iniciar e acessa o link do sistema de testes.
2. **Fazer login:** preenche e-mail e senha e confirma com `Enter`.
3. **Abrir a base de dados:** importa o arquivo `produtos.csv` com o Pandas.
4. **Cadastrar um produto:** preenche os campos `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo` e `obs` e envia o formulário.
5. **Repetir:** executa o passo 4 em um laço (`for`) até acabar a lista de produtos.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Para que foi usada |
|---|---|
| Python 3 | Linguagem do projeto |
| PyAutoGUI | Automação de mouse e teclado (`click`, `write`, `press`, `scroll`) |
| Pandas | Leitura e manipulação do arquivo CSV |
| time | Pausas para aguardar o carregamento das páginas |

---

## 📂 Estrutura do projeto

```
.
├── tarefa.py          # Script principal de automação
├── produtos.csv       # Base de dados com os produtos a cadastrar
├── auxila_posicao.py  # Script auxila pega posição mouse
└── README.md          # Documentação do projeto
```

### Colunas esperadas no `produtos.csv`

`codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`

> O campo `obs` é opcional: se estiver vazio, o script o ignora (`pd.isna`).

---

## ▶️ Como executar

1. Instale as dependências:

   ```bash
   pip install pandas pyautogui
   ```

2. Coloque o arquivo `produtos.csv` na mesma pasta do `tarefa.py`.

3. **Ajuste as coordenadas do mouse** para a sua tela (veja a seção abaixo).

4. Execute o script:

   ```bash
   python tarefa.py
   ```

5. Não mexa no mouse nem no teclado enquanto a automação estiver rodando.

---

## 📍 Ajustando as coordenadas

Os cliques no script usam posições fixas da tela (`x`, `y`), que variam conforme resolução e posição das janelas. Para descobrir as suas, rode no terminal usando arquivo auxila_posicao.py :

```python
import pyautogui, time
time.sleep(5)  # posicione o mouse sobre o local desejado
print(pyautogui.position())
```

Depois, substitua os valores nos `pyautogui.click(x=..., y=...)` do código.

---

## 🛑 Segurança

- O PyAutoGUI possui um **fail-safe**: se algo der errado, mova o mouse rapidamente para o **canto superior esquerdo** da tela para interromper o script.
- Neste projeto, `pyautogui.PAUSE = 2` define uma pausa de 2 segundos entre cada ação, e `time.sleep(4)` garante tempo para o site carregar.

---

## 🚀 Possíveis melhorias

- Substituir coordenadas fixas por reconhecimento de imagem (`pyautogui.locateOnScreen`).
- Adicionar tratamento de erros e registro (log) dos produtos cadastrados.
- Usar variáveis de ambiente para guardar login e senha em vez de deixá-los no código.
- Evoluir para ferramentas de automação web mais robustas, como o Selenium.

---

## 🎓 Créditos

Projeto desenvolvido com base nas aulas do canal **[Hashtag Treinamentos](https://www.youtube.com/@HashtagProgramacao)** no YouTube, como exercício prático de automação com Python.

---

## 👤 Autor

**Luís Henrique Nunes Araújo**
[LinkedIn](https://www.linkedin.com/in/luis-henrique-9953b6302/) • [GitHub](https://github.com/luishenrique456)
