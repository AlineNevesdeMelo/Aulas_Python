idade=int(input('Insira sua idade em anos: '))
renda=float(input('Insira o valor da sua renda: '))
experiência=int(input('Insira o tempo de sua experiência: '))
if idade<18:
    if experiência<6:
        if renda<=1200:
            imposto=0
        else:
            imposto=renda*0.04
    else:
        if experiência>18:
            imposto=renda*0.16
        else:
            imposto=renda*0.14
else:
    imposto=renda*0.22
print('Seu imposto é de R$',str(imposto))