import pyautogui as pa
import time

pa.PAUSE = 0.5

#abrir navegador
pa.press ("win")
pa.write("opera gx")
pa.press("enter")

pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")

time.sleep(2)

pa.click(x=721, y=385)
pa.write("projetoaula1@gmail.com")
pa.press("tab")
pa.write("12345")
pa.press("tab")
pa.press("enter")

import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    
    codigo = str(tabela.loc[linha, "codigo"])
   

    pa.click(x=828, y=273)
    pa.write(codigo)
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")

    pa.write(tabela.loc[linha, "preco_unitario"])
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")
    pa.press("enter")
