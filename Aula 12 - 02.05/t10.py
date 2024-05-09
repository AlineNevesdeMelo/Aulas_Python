menor_numero = None

for i in range(10):
  numero = int(input(f"Digite o {i + 1}º número: "))
  if menor_numero is None or numero < menor_numero:
    menor_numero = numero

print(f"O menor número digitado foi {menor_numero}")