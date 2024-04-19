a=int(input('Valor de A: '))
b=int(input('Valor de B: '))
c=int(input('Valor de C: '))
restoa=a%2
restob=b%2
restoc=c%2

if a>b and a>c and restoa==0:
    if b>c:
        if restob!=0:
            print('A é o maior par e B é o maior impar')
        else:
            if restoc!=0:
                print('A é o maior par e C é o maior impar')
            else:
                print('A é o maior par e não há número impar')
    else:
        if restoc!=0:
            print('A é o maior par e C é o maior impar')
        else:
            if restob!=0:
                print('A é o maior par e B é o maior impar')
            else:
                print('A é o maior par e não há número impar')

elif a>b and a<c and restoc==0:
    if restoa!=0:
        print('C é o maior par e A o maior impar')
    else:
        if restob!=0:
            print('C é o maior par e B o maior impar')
        else:
            print('C é o maior par e não há número impar')

elif b>a and b>c and restob==0:
    if a>c:
        if restoa!=0:
            print('B é o maior par e A o maior impar')
        else:
            if restoc!=0:
                print('B é o maior par e C o maior impar')
            else:
                print('B é o maior par e não há número impar')
    else:
        if restoc!=0:
            print('B é o maior par e C o maior impar')
        else:
            if restoa!=0:
                print('B é o maior par e A o maior impar')
            else:
                print('B é o maior par e não há número impar')

elif b>a and b<c and restoc==0:
    if restob!=0:
        print('C é o maior par')
    else:
        if restoa!=0:
            print('C é o maior par e A o maior impar')
        else:
            print('C é o maior par e não há número impar')
