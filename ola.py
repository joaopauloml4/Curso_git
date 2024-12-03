def calculadora():
    print("Bem-vindo à calculadora!")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    try:
        opcao = int(input("Digite o número da operação desejada (1-4): "))

        if opcao in [1, 2, 3, 4]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                resultado = num1 + num2
                print(f"O resultado da adição é: {resultado}")
            elif opcao == 2:
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            elif opcao == 3:
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            elif opcao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")

# Chamando a função
calculadora()

