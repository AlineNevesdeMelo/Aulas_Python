#Exercício 18 de estudo para P1
saldo = float(input("Informe seu saldo médio: "))
if saldo <= 200:
    credito = 0
elif saldo <= 400:
    credito = saldo*0.2
elif saldo <= 600:
    credito = saldo*0.3
elif saldo > 600:
    credito = saldo*0.4
print("Seu valor final será de R$" + str(round((saldo + credito), 2)) + " com o acrescimo de R$" + str(round(credito, 2)))
