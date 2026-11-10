#PARTE - VIII
#pandas
# 1-2


import pandas as pd

p = pd.DataFrame(
        {"produto": ["Caneta", "Caderno", "Mochila", "Régua"],
        "preco": [1.20, 2.50, 24.90, 0.80], "stock": [50, 3, 7, 2]}
    )
    
#Mostra as primeiras linhas e o resumo com describe().
#Calcula o preço médio.
#Mostra só os produtos com stock abaixo de 5.

print("\nPrimeiras 5 linhas.")
print(p.head())

print("\nDados estatisticos.")
print(p.describe())

print("\nStock abaixo de 5 unidades.")
print(p[p["stock"]<5])




