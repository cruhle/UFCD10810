#PARTE - IV
#dicionario

aluno = {"nome": "Rita", "idade": 22}
print(aluno["nome"])        # Rita
aluno["idade"] = 23         # altera
aluno["cidade"] = "Porto"   # acrescenta

for chave, valor in aluno.items():
    print(chave, "->", valor)

