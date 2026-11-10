#PARTE - IV
#exercicio

"""
Experimenta no teu notebook
Cria um dicionário produto com nome, preço e stock.
Mostra o preço do produto.
Aumenta o stock em 10 unidades.
Mostra todos os pares chave–valor com um for.
"""

produto = {"nome": "batata", "preco": 0.99, "stock":200}

print(produto["preco"])       
produto["stock"] = produto["stock"] + 10

for chave, valor in produto.items():
    print(chave, "->", valor)

