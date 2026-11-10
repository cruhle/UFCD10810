#PARTE - VI
#exercicio

"""
notas = [14, 9, 17, 12, 8]
Mostra cada nota no formato “Nota: 14”.
Conta quantas notas são negativas (menos de 10).
Cria uma lista nova com cada nota mais 1 valor
"""

notas = [14, 9, 17, 12, 8]
negativas = 0

for nota in notas:
    print(f"Nota: {nota:2}")    
    negativas += 1 if nota<10 else 0
    
print(f"QTD notas negativas: {negativas}")

mais_um = [nota + 1 for nota in notas]

#print(mais_um)


