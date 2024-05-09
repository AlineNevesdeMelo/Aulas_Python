#Crie um programa que leia número do usuário até que seja informado um número PAR.
#Dê mensagens ao usuário apropriadas para que ela saiba o que fazer e o que está acontecendo no programa.
print('Esse programa tem como objetivo que o usuário adivinhe, a partir das respostas do programa, \n quais as caracteristicas dos números informados que serão indicados como inválido e válido.')
numero=int(input('Informe um número: '))

while numero%2 != 0:
    print('Número inválido!')
    numero=int(input('Informe outro número: '))
print('Número válido!',numero,' é PAR.')