# Crie um vetor com os nomes de 6 contatos: ["Ana", "Bruno", "Carla", "Daniel", "Eva", "Fábio"].
# Peça ao usuário para substituir o quinto contato por "Elisa".
# Depois, imprima o nome do primeiro e do último contato.

contatos=["Ana", "Bruno", "Carla", "Daniel", "Eva", "Fábio"]
contatos[4]=input('Para substituir seu contato, digite "Elisa": ')
print(f'Seu primeiro contato é {contatos[0]} e o último é {contatos[5]}')