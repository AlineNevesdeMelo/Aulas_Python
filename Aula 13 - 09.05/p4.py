#Experimente o programa a seguir e explique como ele funciona:

senha = input("Digite uma senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")

print("Senha correta! Acesso permitido.")
#Senha é uma variável que armazena a resposta do usuário a pergunta feita.
#While vai iterar a variável senha até que ela senha prenchida corretamente.
#O programa só vai parar se a senha correta for preenchida,
# e quando isso ocorrer, será mostrado ao usuária a resposta "Senha correta! Acesso permitido."