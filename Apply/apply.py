import pandas as pd
import string
import random

df_veiculos = pd.read_csv('veiculos.csv', encoding='ISO-8859-1')

def placa_aleatoria(x):
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return letras + '-' + numeros

# Altera a coluna placa para alterar os valores originais
df_veiculos['PLACA'] = df_veiculos['PLACA'].apply(placa_aleatoria)	