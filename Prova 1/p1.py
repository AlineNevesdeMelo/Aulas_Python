salario_atual=float(input('Salário atual: '))
idade=int(input('Idade: '))
if salario_atual<30:
    salario_acrescido=salario_atual*1.245
else:
    salario_acrescido=salario_atual*1.335
print('Salário acrescido= ',salario_acrescido)