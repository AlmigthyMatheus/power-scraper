import pandas as pd
import os

def salvar_csv(dados, nome_arquivo="dados.csv"):
    df = pd.json_normalize(dados)
    os.makedirs("arquivos", exist_ok=True)
    caminho = os.path.join("arquivos", nome_arquivo)
    df.to_csv(caminho, index=False)
    return caminho

def salvar_excel(dados, nome_arquivo="dados.xlsx"):
    df = pd.json_normalize(dados)
    os.makedirs("arquivos", exist_ok=True)
    caminho = os.path.join("arquivos", nome_arquivo)
    df.to_excel(caminho, index=False)
    return caminho
