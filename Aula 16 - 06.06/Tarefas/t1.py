## Questão 1: Faça um Programa que leia um vetor de 5 números inteiros e depois mostre-os.
vetor = []
for i in range(5):
    num=int(input('Insira um número: '))
    vetor.append(num)
print('Vetor = ',vetor)