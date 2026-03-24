class relacionais:
    def __init__(self, numero):
        self.numero = numero

    def __gt__(self, other):
        return self.numero > other.numero

    def __ge__(self, other):
        return self.numero >= other.numero

    def __it__(self, other):
        return self.numero < other.numero

    def __le__(self, other):
        return self.numero <= other.numero

    def __eq__(self, other):
        return self.numero == other.numero

    def __ne__(self, other):
        return self.numero != other.numero

def menu():
    while True:
        print("Digite dois números:\nA operação será executada na ordem em que os números forem digitados")
        try:
            n1 = relacionais(int(input("Primeiro número: ")))
        except:
            print("Erro!!!\nDigite um número!")
            continue
        try:
            n2 = relacionais(int(input("Segundo número: ")))
        except:
            print("Erro!!!\nDigite um número!")
            continue

        while True:
            print("Selecione uma opção: ")
            print("1 - Igualdade\n2 - Maior que\n3 - Maior ou igual que")
            print("4 - Menor que\n5 - Menor ou igual que\n6 - Diferença:")
            
            try:
                op = int(input(""))
            except:
                print("Digite uma opção válida!")
                break

            match op:
                case 1:
                    print(n1 == n2)
                case 2:
                    print(n1 > n2)
                case 3:
                    print(n1 >= n2)
                case 4:
                    print(n1 < n2)
                case 5:
                    print(n1 <= n2)
                case 6:
                    print(n1 != n2)
                case _:
                    print("Opção inválida!")
            while True:
                try:
                    op2 = int(input("Continuar com o mesmo par de números, ou deseja sair do programa?\n1 - SIM, continuar com par\n2 - NÃO, trocar o par\n3 - Sair do programa\n"))
                    if op2 >= 1 and op2 <= 3:
                        break
                    print("Digite um digito válido!")
                except:
                    print("Digito inválido!")
            if op2 == 2:
                break
            elif op2 == 3:
                print("Até breve!\nFim do programa.")
                return
if __name__ == "__main__":
    menu()
