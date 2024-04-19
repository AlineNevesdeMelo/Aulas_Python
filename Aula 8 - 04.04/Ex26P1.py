#Exercício 26 de estudo para P1
def decompor_valor(valor):

  notas_100 = int(valor // 100)
  resto = valor % 100
  notas_50 = int(resto // 50)
  resto = resto % 50
  notas_10 = int(resto // 10)
  resto = resto % 10
  notas_5 = int(resto // 5)
  notas_1 = resto % 5

  return valor, notas_100, notas_50, notas_10, notas_5, notas_1

# Exemplo de uso
valor = float(input("Digite o valor: "))

valor_original, notas_100, notas_50, notas_10, notas_5, notas_1 = decompor_valor(valor)

print(f"Valor original: R${valor_original:.2f}")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")
