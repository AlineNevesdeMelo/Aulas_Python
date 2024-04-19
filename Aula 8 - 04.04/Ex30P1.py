#Exercício 30 de estudo para P1
def notificar_empresas(indice_poluicao):
  
  notificacoes = {}

  if indice_poluicao <= 0.25:
    notificacoes["grupo_1"] = "Sem notificação."
    notificacoes["grupo_2"] = "Sem notificação."
    notificacoes["grupo_3"] = "Sem notificação."
  elif indice_poluicao <= 0.3:
    notificacoes["grupo_1"] = "**Notificação:** Suspender atividades."
    notificacoes["grupo_2"] = "Sem notificação."
    notificacoes["grupo_3"] = "Sem notificação."
  elif indice_poluicao <= 0.4:
    notificacoes["grupo_1"] = "**Notificação:** Suspender atividades."
    notificacoes["grupo_2"] = "**Notificação:** Suspender atividades."
    notificacoes["grupo_3"] = "Sem notificação."
  else:
    notificacoes["grupo_1"] = "**Notificação:** Suspender atividades."
    notificacoes["grupo_2"] = "**Notificação:** Suspender atividades."
    notificacoes["grupo_3"] = "**Notificação:** Suspender atividades."

  return notificacoes

# Exemplo de uso
indice_poluicao = float(input("Digite o índice de poluição medido: "))

notificacoes = notificar_empresas(indice_poluicao)

for grupo, mensagem in notificacoes.items():
  print(f"{grupo}: {mensagem}")
