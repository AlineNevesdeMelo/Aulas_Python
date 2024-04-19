#Exercício 25 de estudo para P1
def ordenar_valores(i, a, b, c):

  if i == 1:
    a, b, c = sorted([a, b, c])
  elif i == 2:
    a, b, c = sorted([a, b, c], reverse=True)
  elif i == 3:
    maior = max(a, b, c)
    if maior == a:
      if b > c:
        b, c = c, b
    elif maior == b:
      if a > c:
        a, c = c, a
      else:
        b, c = c, b
    else:
      if a > b:
        a, b = b, a

  return a, b, c

# Exemplo de uso
i = int(input("Digite o valor de i: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

a, b, c = ordenar_valores(i, a, b, c)

print(f"Valores ordenados: {a}, {b}, {c}")
