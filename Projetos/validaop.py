def validaop():

    res = 0
    op = None
    n = None

    while True:
        try:
            if op == "nao":
                break
            else:
                op = input("Digite uma operação ou sair para fechar o programa: ")

                if op == "sair":
                    break

                if op != "+" and op != "-" and op != "*" and op != "/":
                    while True:
                        op = input("deseja continuar no programa? ")
                        if op == "sim":
                            break
                        elif op == "nao":
                            break
                        else:
                            print("Você deve digitar sim ou nao: ")
                else:
                    n = int(input("Digite um número: "))

                    if op == "+":
                        res = res + n
                    elif op == "-":
                        res = res - n
                    elif op == "*":
                        res = res * n
                    elif op == "/":
                        if n == 0:
                            print("Você não pode dividir números por zero")
                        else:
                            res = res // n
                    else:
                        break

        except ValueError:
            print("Você deve digitar números!")

    print("O resultado é:", res)
        
        
