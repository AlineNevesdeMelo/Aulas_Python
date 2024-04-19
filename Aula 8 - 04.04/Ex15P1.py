#Exercício 15 de estudo para P1

num=int(input('Digite um número inteiro: '))
resto=num%2
if resto==0:
    paridade='par'
else:
    paridade='ímpar'
if num>0:
    sinal='positivo'
else:
    sinal='negativo'
print('O número ',str(num),'é ',paridade,' e ',sinal)