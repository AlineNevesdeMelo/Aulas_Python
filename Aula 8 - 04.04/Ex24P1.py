#Exercício 24 de estudo para P1
def calcular_duracao_jogo(hora_inicio, hora_final):
  
  if hora_final < hora_inicio:
    diferenca = hora_final + 24 - hora_inicio
  else:
    diferenca = hora_final - hora_inicio

  if diferenca > 24:
    diferenca = 24

  return diferenca

# Exemplo de uso
hora_inicio = int(input("Digite a hora de início do jogo: "))
hora_final = int(input("Digite a hora do final do jogo: "))

duracao = calcular_duracao_jogo(hora_inicio, hora_final)

print(f"A duração do jogo foi de {duracao} horas.")
