cargo=input('Informe seu cargo: ')
nível=int(input('Informe seu nível de acesso: '))
segurança=int(input('Número de segurança: '))
if cargo=='CEO':
    if nível==1:
        if segurança==0:
            tempo=166
        else:
            tempo=150
    else:
        if segurança>0:
            tempo=120
        else:
            tempo=115
else:
    if nível>1:
        tempo=110
    else:
        tempo=106
print('Seu tempo de acesso é de ',str(tempo),' minutos.')