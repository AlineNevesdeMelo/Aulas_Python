#Faça um programa que leia vários número do usuário até que ele informe o número 0 (zero) para terminar.
numero = float(input('Informe o valor do número premiado: '))
while numero != 0:
    print('Errou! Digite 0 (zero) se quiser sair')
    numero=float(input('Digite novamente: '))
print('Isso mesmo! Você acertou!')