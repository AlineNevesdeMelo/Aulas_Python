#Exercício 23 de estudo para P1
import math
def calcular_area_triangulo(a, b, c):
 
  if a > b + c or b > a + c or c > a + b:
    return None

  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return area

# Exemplo de uso
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

area = calcular_area_triangulo(a, b, c)

if area is None:
  print(f"Os valores {a}, {b} e {c} não formam um triângulo.")
else:
  print(f"Os valores {a}, {b} e {c} formam um triângulo.")
  print(f"A área do triângulo é: {area:.2f}")
