#PARTE - III
#lista

temperaturas = [18, 21, 25, 19, 23]

#Mostra a temperatura mais alta e a mais baixa.
print(f"Temperaturas MAX: {max(temperaturas)} MIN:{min(temperaturas)}")

#Calcula a temperatura média.
print(f"Temperatura MEDIA: {sum(temperaturas)/len(temperaturas):.2f}")

#Acrescenta 20 à lista e mostra quantas temperaturas tem agora.
print(f"QTD de temperaturas: {len(temperaturas)} antes de ")
temperaturas.append(20)
print(f"QTD de temperaturas: {len(temperaturas)} depois de")
print(f"Temperatura MEDIA: {sum(temperaturas)/len(temperaturas):.2f}")

