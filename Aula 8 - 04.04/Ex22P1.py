#Exercício 22 de estudo para P1
def calcular_novo_salario(salario_antigo, codigo_cargo):

  tabela_cargos = {
    101: {"percentual": 10},
    102: {"percentual": 20},
    103: {"percentual": 30},
  }

  if codigo_cargo in tabela_cargos:
    percentual_aumento = tabela_cargos[codigo_cargo]["percentual"]
  else:
    percentual_aumento = 40

  aumento = salario_antigo * percentual_aumento / 100
  novo_salario = salario_antigo + aumento
  diferenca = novo_salario - salario_antigo

  return salario_antigo, novo_salario, diferenca

# Exemplo de uso
salario_antigo = float(input("Digite o salário antigo: "))
codigo_cargo = int(input("Digite o código do cargo: "))

salario_antigo, novo_salario, diferenca = calcular_novo_salario(
    salario_antigo, codigo_cargo
)

print(f"Salário antigo: R${salario_antigo:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
print(f"Diferença: R${diferenca:.2f}")
