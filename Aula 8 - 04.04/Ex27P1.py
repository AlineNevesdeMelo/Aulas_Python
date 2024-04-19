#Exercício 27 de estudo para P1
def calcular_valor_total(ipi, codigo_peca1, valor_unitario_peca1, quantidade_peca1, codigo_peca2, valor_unitario_peca2, quantidade_peca2):

  valor_total_peca1 = valor_unitario_peca1 * quantidade_peca1
  valor_total_peca2 = valor_unitario_peca2 * quantidade_peca2
  valor_total = valor_total_peca1 + valor_total_peca2

  valor_ipi = valor_total * (ipi / 100)
  valor_total_a_ser_pago = valor_total + valor_ipi

  return valor_total_a_ser_pago

# Exemplo de uso
ipi = float(input("Digite a percentagem do IPI: "))
codigo_peca1 = int(input("Digite o código da peça 1: "))
valor_unitario_peca1 = float(input("Digite o valor unitário da peça 1: "))
quantidade_peca1 = int(input("Digite a quantidade de peças 1: "))
codigo_peca2 = int(input("Digite o código da peça 2: "))
valor_unitario_peca2 = float(input("Digite o valor unitário da peça 2: "))
quantidade_peca2 = int(input("Digite a quantidade de peças 2: "))

valor_total = calcular_valor_total(ipi, codigo_peca1, valor_unitario_peca1, quantidade_peca1, codigo_peca2, valor_unitario_peca2, quantidade_peca2)

print(f"Valor total a ser pago: R${valor_total:.2f}")
