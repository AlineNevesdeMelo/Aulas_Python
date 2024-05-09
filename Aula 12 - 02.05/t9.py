maior_numero = None #significa que ela ainda não possui um valor definido

for i in range(10):
  numero = int(input(f"Digite o {i + 1}º número: "))
  if maior_numero is None or numero > maior_numero:
    maior_numero = numero

print(f"O maior número digitado foi {maior_numero}")