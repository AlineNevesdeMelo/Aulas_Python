#Explique o programa a seguir, em especial as funções startwith e lower.
#Depois, pesquise o endswith e adicione um novo FOR para mostrar as letras que terminam com A


# Criar um vetor para armazenar as strings
strings = []

# Ler as strings do usuário
for i in range(6):
    string = input(f"Digite a string {i+1}: ")
    strings.append(string) # .append inclui o elemento no vetor

# Imprimir as strings que começam com 'A'
print("Strings que começam com 'A':")
for string in strings:
    if string.lower().startswith('a'):
        # lower: Coloca toda a string em minúscula
        # startswith: determina se uma string começa com os caracteres especificados, retornando true ou false
        print('Palavras que começam com A: ',string)

        # endswith: verifica se uma string termina com um determinado sufixo (última silaba/letra da palavra)
for string in strings:
    if string.lower().endswith('a'):
        print('Palavras que terminam com A: ',string)