salário=float(input('Salário: '))
beneficio=salário*0.1
desconto=salário*0.06
total=salário+beneficio-desconto
if total<1500:
    imposto=0
    print('Não tera imposto e seu salário será de ',total)
else:
    imposto=total*0.1
    total2=total-imposto
    print('Será cobrado 10% de imposto e seu salário será de ',total2)