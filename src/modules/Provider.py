import pandas as pd

dataFile = pd.read_excel('params.xlsx')
keywords = dataFile["palavras_chave"].dropna().to_numpy()
urls = dataFile["urls"].dropna().to_numpy()