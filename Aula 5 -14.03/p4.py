#Faça um programa que leia do usuário: -população atual;-Taxa de crescimento;-Anos.
#PopulaçãoFutura=populaçãoatual*(1+taxadecrescimento)**anos

import math
populaçãoatual=int(input('Qual a população atual? '))
taxadecrescimento=float(input('Informe a taxa de crescimento (ex: 5 para 5%): '))
anos=int(input('Informe a quantidade de anos: '))
B=anos
A=(1+(taxadecrescimento/100))
populaçãofutura=populaçãoatual*math.pow(A,B)
print('A estimativa de população futura é de ',populaçãofutura)
