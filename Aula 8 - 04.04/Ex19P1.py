#Exercício 19 de estudo para P1
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
tipo = int(input("Informe o tipo de média que você deseja: "))
if tipo == 1:
    media = (nota1 + nota2 + nota3)/3
elif tipo == 2:
    media = nota1*0.3 + nota2*0.3 + nota3*0.4
elif tipo == 3:
    media = 3/(nota1/(nota1**2) + nota2/(nota2**2) + nota3/(nota3**2))
print("A média será de " + str(round(media, 2)))
