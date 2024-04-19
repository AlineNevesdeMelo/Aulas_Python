#Exercício 14 de estudo para P1

nota1=float(input('Nota 1: '))
nota2=float(input('Nota 2: '))
nota3=float(input('Nota 3: '))
if nota1>=nota2:
    if nota1>nota3:
        media=((nota1*4)+(nota2*3)+(nota3*3))/4+3+3
        print('Nota 1 =',str(nota1),' - Nota 2=',str(nota2),' - Nota 3=',str(nota3))
        print('média pond. = ((',str(nota1),'*4)+(',str(nota2),'*3)+(',str(nota3),'*3))/4+3+3')
        print('média pond.= ',str(media))
    else:
        media=((nota1*3)+(nota2*3)+(nota3*4))/4+3+3
        print('Nota 1 =',str(nota1),' - Nota 2=',str(nota2),' - Nota 3=',str(nota3))
        print('média pond. = ((',str(nota1),'*3)+(',str(nota2),'*3)+(',str(nota3),'*4))/4+3+3')
        print('média pond.= ',str(media))
else:
    if nota2>nota3:
        media=((nota1*3)+(nota2*4)+(nota3*3))/4+3+3
        print('Nota 1 =',str(nota1),' - Nota 2=',str(nota2),' - Nota 3=',str(nota3))
        print('média pond. = ((',str(nota1),'*3)+(',str(nota2),'*4)+(',str(nota3),'*3))/4+3+3')
        print('média pond.= ',str(media))
    else:
        media=((nota1*3)+(nota2*3)+(nota3*4))/4+3+3
        print('Nota 1 =',str(nota1),' - Nota 2=',str(nota2),' - Nota 3=',str(nota3))
        print('média pond. = ((',str(nota1),'*3)+(',str(nota2),'*3)+(',str(nota3),'*4))/4+3+3')
        print('média pond.= ',str(media))