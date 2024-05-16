#Faça o programa a seguir:

dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"]
numero = int(input("qual dia quer saber?"))

#Aprimore este programa para não permitir o usuário informar um número que extrapole as dimensões do vetor.
if numero>7:
    print("Valor inválido")
else:
    print(dias[numero-1])