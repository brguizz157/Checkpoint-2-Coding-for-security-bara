print("Calculadora — digite 'sair' para encerrar.\n")

while True:
    entrada1 = input("Primeiro número: ")

    if entrada1.lower() == "sair":
        print("Encerrando calculadora.")
        break

    try:
        num1 = float(entrada1)
        num2 = float(input("Segundo número: "))
        operacao = input("Operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2
        else:
            raise ValueError("operação inválida")

    except ValueError:
        print("Erro: número inválido ou operação não reconhecida.\n")

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.\n")

    else:
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}\n")

    finally:
        print("Operação processada.")
