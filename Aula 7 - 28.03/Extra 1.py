altura=float(input('Insira sua altura: '))
peso=float(input('Insira seu peso: '))
imc=peso/(altura**2)

if imc>=18.6 and imc<=24.9:
    print('Peso ideal')
elif imc<18.5:
    print('Abaixo de peso')
elif imc>=25 and imc<=29.9:
    print('Levemente acima do peso')
elif imc>=30 and imc<=34.9:
    print('Obesidade grau I')
elif imc>=35 and imc<=39.9:
    print('Obesidade grau II (severa)')
elif imc>40:
    print('Obesidade III (mórbida)')