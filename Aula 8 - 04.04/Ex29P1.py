#Exercício 29 de estudo para P1
def calcular_media_aproveitamento(numero_aluno, nota1, nota2, nota3, media_exercicios):

  media_aproveitamento = (nota1 + 2 * nota2 + 3 * nota3 + media_exercicios) / 7

  if media_aproveitamento >= 9.0:
    conceito = "A"
  elif media_aproveitamento >= 7.5:
    conceito = "B"
  elif media_aproveitamento >= 6.0:
    conceito = "C"
  elif media_aproveitamento >= 4.0:
    conceito = "D"
  else:
    conceito = "E"

  if conceito in ("A", "B", "C"):
    mensagem = "APROVADO"
  else:
    mensagem = "REPROVADO"

  return {
      "numero_aluno": numero_aluno,
      "notas": [nota1, nota2, nota3],
      "media_exercicios": media_exercicios,
      "media_aproveitamento": media_aproveitamento,
      "conceito": conceito,
      "mensagem": mensagem,
  }

# Exemplo de uso
numero_aluno = int(input("Digite o número do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

aluno = calcular_media_aproveitamento(numero_aluno, nota1, nota2, nota3, media_exercicios)

print(f"Número do aluno: {aluno['numero_aluno']}")
print(f"Notas: {aluno['notas']}")
print(f"Média dos exercícios: {aluno['media_exercicios']}")
print(f"Média de aproveitamento: {aluno['media_aproveitamento']}")
print(f"Conceito: {aluno['conceito']}")
print(f"Mensagem: {aluno['mensagem']}")
