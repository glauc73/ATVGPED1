def cpfIncompleto():
    cpf = int(input("Digite o CPF incompleto: "))
    if len(str(cpf)) != 9:
        print("Ops, um erro!!!\nO CPF a ser completado deve ter apenas 9 digitos, sem letras, pontos ou travessões!\n")
        return
    num = []

    for i in range(9):
        num.append(cpf % 10)
        cpf = cpf // 10

    def dig(x, l = num):
        sum = 0
        for i in range(9):
            sum += l[i] * (i + x)
        y = sum % 11
        if y <= 1:
            return 0
        else:
            return 11 - y

    print("Resultado do CPF: ")
    print(f"{num[8]}{num[7]}{num[6]}.{num[5]}{num[4]}{num[3]}.{num[2]}{num[1]}{num[0]}-{dig(2)}{dig(3)}\n")

def cpfAnalise():
    acpf = int(input("CPF a ser analisado: "))
    if len(str(acpf)) != 9:
        print("Ops, um erro!!!\nCPF deve ter a ser analisado deve ter apenas 11 números, sem letras, pontos ou travessões!\n")
    num2 = []
    def dig(x, l = num2):
        sum = 0
        for i in range(9):
            sum += l[i] * (i + x)
        y = sum % 11
        if y <= 1:
            return 0
        else:
            return 11 - y

    dupla = acpf % 100
    acpf = acpf // 100
    for i in range(9):
        num2.append(acpf % 10)
        acpf = acpf // 10

    d1 = dig(2, num2)
    d2 = dig(3, num2)

    if dupla // 10 == d1 and dupla % 10 == d2:
        print("CPF válido.\n")
    else:
        print("CPF inválido.")
        print(f"CPF válido deveria ser: {num2[8]}{num2[7]}{num2[6]}.{num2[5]}{num2[4]}{num2[3]}.{num2[2]}{num2[1]}{num2[0]}-{dig(2)}{dig(3)}\n\n")

def menu():
    print("Bem vindo! Selecione a opção desejada:\n1 - Cálculo dos digitos finais do cpf.\n2 - Analise de validade do cpf.\n3 - Sair")
    while True:
        try:
            op = int(input(""))
        except:
            print("Opção inválida!\nPor favor, digite um dos dígitos disponíveis!\n")
        match op:
            case 3:
                break
            case 1:
                try:
                    cpfIncompleto()
                except:
                    print("Digite o CPF a ser complementado corretamente!\n(Nove números sem espaço, pontos ou travessão.)\n\n")
            case 2:
                try:
                    cpfAnalise()
                except:
                    print("Digite o CPF a ser complementado corretamente!\n(Nove números sem espaço, pontos ou travessão.)\n")
            case _:
                print("Opção indisponível!\n")
        print("Selecione a opção desejada:\n1 - Cálculo dos digitos finais do cpf.\n2 - Análise de validade do cpf.\n3 - Sair")

if __name__ == "__main__":
    menu()
