from calculadora_completa import CalculadoraCompleta

calc = CalculadoraCompleta()

while True:
    print("\nSelecione a operação que deseja realizar:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz")
    print("7 - Fatorial")
    print("8 - Converter Celsius para Fahrenheit")
    print("9 - Converter Fahrenheit para Celsius")
    print("10 - Ver Histórico")
    print("11 - Limpar Histórico")
    print("0 - Sair")

    op = input("Digite o número da operação: ")

    if op == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", calc.soma(a, b))

    elif op == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", calc.subtracao(a, b))

    elif op == "3":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", calc.multiplicacao(a, b))

    elif op == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        try:
            print("Resultado:", calc.divisao(a, b))
        except ArithmeticError as e:
            print(e)

    elif op == "5":
        a = float(input("Digite a base: "))
        b = float(input("Digite o expoente: "))
        try:
            print("Resultado:", calc.potencia(a, b))
        except ArithmeticError as e:
            print(e)

    elif op == "6":
        a = float(input("Digite o número: "))
        indice = float(input("Digite o índice da raiz: "))
        try:
            print("Resultado:", calc.raiz(a, indice))
        except ArithmeticError as e:
            print(e)

    elif op == "7":
        a = int(input("Digite um número inteiro não negativo: "))
        try:
            print("Resultado:", calc.fatorial(a))
        except ValueError as e:
            print(e)

    elif op == "8":
        celsius = float(input("Digite a temperatura em Celsius: "))
        print("Resultado:", calc.celsiusParaFahrenheit(celsius))

    elif op == "9":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print("Resultado:", calc.fahrenheitParaCelsius(fahrenheit))

    elif op == "10":
        historico = calc.getHistorico()
        if len(historico) > 0:
            print("\nHistórico de Operações:")
            for item in historico:
                print(item)
        else:
            print("Histórico vazio.")

    elif op == "11":
        calc.limparHistorico()
        print("Histórico limpo.")

    elif op == "0":
        print("Finalizando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")