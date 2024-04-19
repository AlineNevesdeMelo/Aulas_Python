#Exercício 28 de estudo para P1
def calcular_duracao_jogo(hora_inicio_hora, hora_inicio_minuto, hora_fim_hora, hora_fim_minuto):

  diferenca_minuto = hora_fim_minuto - hora_inicio_minuto
  if diferenca_minuto < 0:
    diferenca_minuto += 60
    hora_fim_hora -= 1

  diferenca_hora = hora_fim_hora - hora_inicio_hora
  if diferenca_hora > 24:
    diferenca_hora = 24

  return diferenca_hora, diferenca_minuto

# Exemplo de uso
hora_inicio_hora = int(input("Digite a hora de início do jogo (hora): "))
hora_inicio_minuto = int(input("Digite a hora de início do jogo (minuto): "))
hora_fim_hora = int(input("Digite a hora do término do jogo (hora): "))
hora_fim_minuto = int(input("Digite a hora do término do jogo (minuto): "))

duracao_hora, duracao_minuto = calcular_duracao_jogo(hora_inicio_hora, hora_inicio_minuto, hora_fim_hora, hora_fim_minuto)

print(f"A duração do jogo foi de {duracao_hora} horas e {duracao_minuto} minutos.")
