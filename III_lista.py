#PARTE - III
#lista

notas = [14, 9, 17, 12]
print(notas[0])                 # 14 primeira
print(notas[-1])                # 12 última
print(notas[1:3])               # [9, 17]

notas.append(15)                # acrescenta no fim
print(len(notas))               # 5
print(sum(notas) / len(notas))  # 13.4
print(sorted(notas))            # [9, 12, 14, 15, 17]

