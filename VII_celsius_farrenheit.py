#PARTE - VII
#celsius_farrenheit

"""
converter_celsius(c), que devolve a temperatura em Fahrenheit (c × 9 / 5 + 32).
Testa-a com 0 e com 100.
e_positiva(nota), que devolve True se a nota for 10 ou mais.
"""

def converter_celsius(celsisu):
    return ((celsisu*9)/5 + 32)
    
valores_celsisus = [0,10,20,30,40,50,60,70,80,90,100,110]

for vlr in valores_celsisus:
    print(f"Celsius: {vlr:3} equivale em Fahrenheit: {converter_celsius(vlr):6.2f}")





