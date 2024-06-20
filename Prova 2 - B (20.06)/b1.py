# Inverter um vetor de nomes sem utilizar funções prontas do Python
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e imprima o vetor de nomes  invertido. Por exemplo, se o vetor original for ['Andre', 'Joao', ' Mauro'], o programa deve imprimir ['Mauro', 'Joao', 'Andre'].
Vetor=[]
N=int(input('Insira o valor de N: '))

for i in range(N):
    nomes=input('Insira um nome: ')
    Vetor.append(nomes)

Vetor_invertido=Vetor[::-1]
print(f'Vetor original = {Vetor}')
print(f'Vetor invertido = {Vetor_invertido}')