#### Exercício 1
Crie um programa que leia a idade e a altura.
Condicional:
````
Se idade >17:
    se altura>160
        bolsa=1120
    senão:
        bolsa=1410
senão:
    bolsa=1439
````
#
#### Exercício 2
Crie um programa que leia o saldo e dias. Condicional:
````
Se saldo<0:
    se dias<30:
        saldo=saldo*1.04
    senão:
        saldo=saldo+(0.8)**dias
senão:
    se dias<30:
        saldo=saldo*1.08
    senão:
        saldo=saldo+(0.7)**dias
````
#
#### Exercício 3
Crie um programa que leia x1, x2 e y1,y2 e calcule:
````
Δ1=(x2-x1)²
Δ2=(y2-y1)²

Se Δ1>Δ2:
    se x1>x2:
        alfa=Δ1*(x1)²
    senão:
        alfa=Δ1*(x2)²
senão:
    alfa=(Δ2-Δ1)²
````
#
#### Exercício 4
Crie um programa que leia o total e a série da nota fiscal. Condicional:
````
Se serie=='E1':
    se total>180:
        imposto=total*0.17
    senão:
        imposto=total*0.14
senão:
    se total>199:
        imposto=total*0.18
    senão:
        imposto=total*0.16
````
#
#### Exercício 5
Crie um programa que leia os valores: aluguel, área e total.
Condicional:
````
Se área>50:
    se total>350000
        se aluguel>1800
            preço=aluguel*12+total
        senão:
            preço=aluguel*6+total
    senão:
        preço=aluguel+total
senão:
    preço=total*1.12
````
#
#### Exercício 6
Crie um programa que leia idade, renda e experiência.
Condicional:
````
se idade<18:
    se experiência<6:
        se renda<=1200:
            imposto=0
        senão:
            imposto=renda*0.04
    senão:
        se experiência>18:
            imposto=renda*0.16
        senão:
            imposto=renda*0.14
senão:
    imposto=renda*0.22
````
#
#### Exercício 7
Crie um programa que leia o cargo, nível de acesso e segurança do usuário. Condicional:
````
se cargo=='CEO':
    se nível==1:
        se segurança==0:
            tempo=166
        senão:
            tempo=150
    senão:
        se segurança>0:
            tempo=120
        senão:
            tempo=115
senão:
    se nível>1:
        tempo=110
    senão:
        tempo=106
````
#
#### Exercício 8
Crie um programa que leia o total e a quantidade de itens do usuário. Condicional:
````
if itens>10 and total>100:
    desconto=total*0.15
else:
    desconto=total*0.06
````
#
#### Exercício 9
Crie um programa que leia o tempo e idade do usuário.
Condicional:
````
if idade>65 or tempo>35:
    aposentadoria=100/100
else:
    aposentadoria=75/100
````