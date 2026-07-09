import pyautogui
import time
import pandas
import openpyxl
#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho (hotkey)
#--------------------------------------
# Passo 1: Entrar no sistema da empresa
#abrir o naveg123134ador
pyautogui.press ("win")
time.sleep (2)
pyautogui.write ("opera")
pyautogui.press ("enter")

time.sleep (2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login
pyautogui.click (x=719, y=395)
pyautogui.write ("123134")

pyautogui.clic123134k(x=697, y=493)
pyautogui.write ("123456")


pyautogui.press ("enter")

time.sleep(3)
# Passo 3: Abrir a base de dados
tabela = pandas.read_csv ("produtos.csv")
print (tabela)
# Passo 4: Cadastrar  1 produto
for linha in tabela.index:
    pyautogui.click (x=760, y=273)
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write (codigo)
    pyautogui.press ("tab")

    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write (marca)
    pyautogui.press ("tab")

    tipo = str (tabela.loc [linha, "tipo"])
    pyautogui.write (tipo)
    pyautogui.press ("tab")

    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write (categoria)
    pyautogui.press ("tab")

    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write (preco_unitario)
    pyautogui.press ("tab")

    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write (custo)
    pyautogui.press ("tab")


    obs = str (tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write (obs)
    pyautogui.press ("tab")

    pyautogui.press ("tab")
    pyautogui.press ("enter")
    pyautogui.scroll (5000)
# Passo 5: Repetir o "passo 4" até acabar todos os prdutos

