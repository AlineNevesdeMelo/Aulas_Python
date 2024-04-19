prova=float(input('Nota da prova: '))
trabalho=float(input('Nota do trabalho: '))
seminário=float(input('Nota do seminário: '))
média=prova*0.4+trabalho*0.3+seminário*0.3
if média>=7.0:
    print('Aprovado')
else:
    print('Reprovado')