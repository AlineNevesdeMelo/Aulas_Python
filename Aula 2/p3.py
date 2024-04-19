#Faça um programa que leia:
#-Nota do TCC
#-Nota da prova;
#-Nota do trabalho:
#Calcule a média: MÉDIA = TCC*0.3+prova*0.5+trabalho*0.2

TCC=float(input('Nota do TCC: '))
prova=float(input('Nota da prova: '))
trabalho=float(input('Nota do trabalho: '))
MédiaPonderada=(TCC*0.3)+(prova*0.5)+(trabalho*0.2)
print('Média = '+str(MédiaPonderada))
