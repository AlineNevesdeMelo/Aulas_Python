#Um programa de adivinhação

#Faça um programa que tenha um while (numero != 55) e dentro do while leia peça para o usuário tentar adivinhar um número. 
#O laço deve continuar até o usuário adivinhar que o número é o 55.
numero=0
while numero != 55:
    numero=float(input('Teste sua sorte! Adivinhe o número premiado! R: '))
    if numero != 55:
        print('Errou! Tente novamente.')
print('Você acertou!')