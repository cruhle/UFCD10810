#PARTE - VI
#ciclo

for i in range(1, 4):
    print(f"Range (1..4) - {i}")                               # 1, 2, 3
    
notas = [14, 9, 17]
for nota in notas:
    print(f"Dobro das notas: {nota:2} - {nota * 2}")    # 28, 18, 34
    
dobros = [n * 2 for n in notas]     # numa linha

# print(dobros)

