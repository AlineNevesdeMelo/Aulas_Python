tempo=int(input('Insira o tempo: '))
idade=int(input('Insira sua idade: '))
if idade>65 or tempo>35:
    aposentadoria=100/100
else:
    aposentadoria=75/100
print('Sua aposentadoria será: ',str(aposentadoria))