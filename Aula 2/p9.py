#Faça um programa que leia do usuário o salário.
#Calcule o imposto=salário*0.15
#Calcule o INSS=salario*0.17
#Calcule o valor=salário-imposto-INSS
#Mostre a mensagem adequada.

salário=float(input('Qual o seu salário? '))
imposto=salário*0.15
INSS=salário*0.17
valor=salário-imposto-INSS
print('Salário liquido = '+str(round(valor,2))+' reais')
