nascimento=int(input('Ano de nascimento: '))
ano_atual=int(input('Ano atual: '))
idade_anos=ano_atual-nascimento
idade_horas=idade_anos*365*24
idade_minutos=idade_horas*60
idade_semanas=(idade_anos*365)/4 #um mês com 4 semanas
print('Sua idade em anos é: ',str(idade_anos))
print('Sua idade em horas é: ', str(idade_horas))
print('Sua idade em minutos é: ',str(idade_minutos))
print('Sua idade em semana é: ',str(idade_semanas))