#Teste o programa a seguir e explique como ele funciona:

operacao = ""

while operacao != "sair":
    operacao = input("Digite 'soma' para somar, 'multiplicacao' para multiplicar ou 'sair' para encerrar: ").lower()

    if operacao == "soma":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")

    elif operacao == "multiplicacao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")

    elif operacao == "sair":
        print("Encerrando a calculadora...")

    else:
        print("Operação inválida. Tente novamente.")
#O programa pede que o usuário informe a operação que ele deseja realizar.
#De acordo com a operação informada ele processa a condição para que a operação seja realizada.
#Como no caso da operação soma, o programa pergunta ao usuário os dois valores que ele deseja
#e em seguida ele retorna o resultado.