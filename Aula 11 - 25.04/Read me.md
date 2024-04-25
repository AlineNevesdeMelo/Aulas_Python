## Aula introdutória do FOR (25/04/2024)
### Atividade 1
Escreva um programa que imprima os números de 1 a 10 usando um laço FOR.

Solução
````
for numero in range(1, 11): 
   print(numero)
````

- adicione comentários ao programa explicando como ele funciona. Como é seu comportamento e como você entende o funcionamento do FOR
#
### Atividade 2
Faça um programa que leia o nome do usuário e mostre esse nome 10 vezes.
#
### Atividade 3
Criar um programa que mostre 20 vezes a mensagem:
````
"Eu estou criando uma mente algorítmica e me aperfeiçoando"
````
#
### Atividade 4
Execute o programa a seguir e explique o que ele faz:
````
for numero in range(1, 11): 
    resultado = 5 * numero
    print(str(resultado))
````
#
### Atividade 5
Alterar o programa a seguir da tabuada do 5 para uma versão geral.
````
for i in range(1, 11): 
    resultado = 5 * i 
    print(str(resultado))
````
Pergunte para o usuário qual a tabuada que ele quer e utilize no lugar do 5.
#
### Atividade 6
Escreva um programa que mostre os número pares entre 1 e 20
````
for num in range(1, 21): 
     if num % 2 == 0: 
           print (num)
````
Rode, explique o programa e tire print.
#
### Atividade 7
Altere o programa a seguir para mostrar os número ÍMPARES entre 1 e 20
````
for num in range(1, 21): 
     if num % 2 != 0: # O resto da divisão por 2 o resultado tem que ser diferente de zero.
           print (num)
````
Explique a alteração que vocês fez. Tire print e envie.
#
### Atividade 8
Faça um programa que leia um numero N e o NOME do usuário.
Utilize o FOR para mostrar o NOME do usuário N vezes.
````
Solução: 
n=int(input('Insira a quantidade n: '))
nome=input('Digite um nome: ')
for n in range(1,n+1):
    print(nome)
````

#
### Atividade 9
- Conceito de SOMATÓRIA

Escreva um algoritmo que calcule a soma dos números de 1 a 15.
````
soma = 0
for num in range(1, 16): 
     soma += num 

print("A somatória de 1 a 15 é: ", soma)
````
RODE E EXPLIQUE PORQUE A VARIÁVEL SOMA É INICIALIZADA COM ZERO?
#
### Atividade 10
O Programa a seguir faz a SOMATÓRIA de número de 1 a 15.
````
soma = 0
for num in range(1, 16): 
     soma += num 

print("A somatória de 1 a 15 é: ", soma)
````
Altere para que ele faça o produtório de 1 a 15.
#
### Atividade 11
Faça um programa que leia a idade de 5 pessoas e exiba a soma das idades.
````
Dica:
1- inicialize a variável soma=0
2- faça o for de 1 a 6
3- dentro do for leia a idade
4- soma a idade soma+=idade
5- fora do for, mostre a soma
````
#
### Atividade 12
Altere o programa anterior que realiza a soma das idade, para que ele calcule a MÉDIA das idades.
````
Solução:
soma=0
for i in range(1,6):
    Idade=int(input('Insira sua idade: '))
    soma += Idade
print(soma/5)
````
#
