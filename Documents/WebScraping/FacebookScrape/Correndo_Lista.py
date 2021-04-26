import pandas as pd
from first_fbscrape import correr_API
from os import path


lista = pd.read_csv('Lista Alfredo.csv')
total_lines = lista.shape
linhas = total_lines[0]
nomedaplanilha = input('Qual o nome do arquivo?')

if not path.isdir(f"{nomedaplanilha}.csv"):
    df = pd.DataFrame(columns=['User_ID', 'Nome_Completo', 'User_URL'])
    df.to_csv(f"{nomedaplanilha}.csv", index=False)
else:
    pass


for i in range(linhas):
    if i > 0:
    #if i> 25:
        correr_API(lista['FB URL'][i])
    else:
        pass
