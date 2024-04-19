#Faça um programa que leia:
#O total da compra;
#O valor do desconto;
#O valor dos juros;
#Calcule a conta total: Conta=Total-Desconto+Juros

Tcompra=float(input('Insira o valor total da compra: '))
Desconto=float(input('Insira o valor do desconto: '))
Juros=float(input('Insira o valor dos juros: '))
Conta=Tcompra-Desconto+Juros
print('O total da compra é de '+str(Conta)+' reais')
