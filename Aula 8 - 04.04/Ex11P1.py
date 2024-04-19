#Exercício 11 de estudo para P1

a=int(input('Insira o valor de A: '))
b=int(input('Insira o valor de B: '))
resto=a%b #O operador % calcula o resto da divisão de um número por outro.
if resto==0:
    print('São múltiplos')
else:
    print('Não são múltiplos')