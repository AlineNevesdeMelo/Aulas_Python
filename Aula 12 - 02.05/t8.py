par_count = 0

for i in range(10):
  numero = int(input(f"Digite o {i + 1}º número: "))
  if numero % 2 == 0:
    par_count += 1

print(f"Foram digitados {par_count} números pares.")