#Faça um programa que leia o total da conta do restaurante.
#-Calcule a gorjeta de 10%: gorjeta=total*(10/100)
#-Calcule a conta com a gorjeta: conta=total+gorjeta
#Mostre o resultado

total=float(input('Informe o gasto total do cliente: '))
gorjeta=total*(10/100)
conta=total+gorjeta
print('Conta = '+str(round(conta,2))+' reais')
