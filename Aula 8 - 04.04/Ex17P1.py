#Exercício 17 de estudo para P1
altura = float(input("Informe sua altura em metros: "))
genero = input("Informe seu gênero: ")
if genero == "Masculino":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print("Seu peso ideal é de " + str(round(peso, 2)) + "Kg")

