preço=float(input('Preço do produto: '))
if preço<50:
    valor=preço*0.9
else:
    valor=preço*0.8
print('valor= ',str(valor))