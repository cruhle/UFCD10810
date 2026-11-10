#PARTE - V
#exercicio

"""
Cria uma variável saldo com o valor 30.
Mostra “Sem saldo” se o saldo for 0 ou menos.
Mostra “Saldo baixo” se for menos de 50.
Nos outros casos, mostra “Saldo OK”. Testa com 0, 30 e 80.
"""

saldos = [0,30,80]

for saldo in saldos:
    
    if saldo < 1:
        res = "Sem saldo"
    elif saldo < 51:
        res = "Saldo baixo"
    else:
        res = "Saldo OK"
        
    print(f"Saldo disponivel: {saldo:02} - {res}")


