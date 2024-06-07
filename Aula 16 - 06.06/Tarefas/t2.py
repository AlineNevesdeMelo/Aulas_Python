# Questão 2: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for i in range(10):
    num_real=float(input('Insira um número: '))
    vetor.append(num_real)
print('Vetor original = ',vetor)

# Primeira forma: Fatiamento de listas (Slicing)
vetor_invertido=vetor[::-1]
print('Vetor invertido = ',vetor_invertido)

# Segunda forma: Utilizando a função "Reversed"
vetor_invertido2=list(reversed(vetor))
print('Vetor invertido = ',vetor_invertido2)