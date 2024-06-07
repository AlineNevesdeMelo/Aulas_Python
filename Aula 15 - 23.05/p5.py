#Faça um Programa que leia um vetor de 10 caracteres (letras)
#Faça um FOR que verifique quantas vogais estão no vetor. Imprima essas vogais presentes no vetor.

letras = []
vogais = []

for i in range (10):
    letra=input('Insira uma letra: ')
    letras.append(letra.lower())

quant_vogal=0

for i in letras:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        quant_vogal+=1
        vogais.append(i)

print('Quantidade de vogais: ',quant_vogal)
print('Vogais: ',vogais)