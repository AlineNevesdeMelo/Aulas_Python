x1=float(input('Insira x1: '))
x2=float(input('Insira x2: '))
y1=float(input('Insira y1: '))
y2=float(input('Insira y2: '))
Δ1=(x2-x1)**2
Δ2=(y2-y1)**2
if Δ1>Δ2:
    if x1>x2:
        alfa=Δ1*(x1)**2
    else:
        alfa=Δ1*(x2)**2
else:
    alfa=(Δ2-Δ1)**2
print('Alfa=',str(alfa))