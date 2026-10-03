# Projeto de tarefa com automação (pyautogui) e pandas (ler base de dados)
# passo 1 :  Entrar no sistema da empresa
# passo 2 : fazer login
# passo 3 : Abrir a base de dados (importar arquivo produtos.csv)
# passo 4 : Cadastrar 1 produto
# passo 5 : Repetir o passo 4 até acabar a lista de produtos
# pyautogui.click : clica
# pyautogui.write : escreve um texto
# pyatogui.press : aperta um atalho teclado
# pyautogui.hotket("ctrl","c") : aperta um atalho 
import pandas as pd
import pyautogui
import time
pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=557,y=486)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# fazer pausa maior pro site carregar
time.sleep(4)
pyautogui.click(x=664,y=469)
pyautogui.write("lu1s@gmail.com")
pyautogui.press("tab") #passar para o próximo campo
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)
tabela = pd.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
    pyautogui.click(x=615,y=324)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")# passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter") #clica botão envia
    pyautogui.scroll(5000) # voltar para o inicio tela
