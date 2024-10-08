usuarios = []
contas = []
agencia = []
numero_conta = []


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação Negada! Saldo Insuficiente.")
    elif excedeu_limite:
        print("Operação Negada! O valor do saque excede o limite de R$ 500,00.")
    elif excedeu_saques:
        print("Operação Negada! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação Negada! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===================================")


def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado com esse CPF!")
            return

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def criar_conta_corrente(cpf):
    global numero_conta
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado!")
        return
    
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    contas.append(conta)
    numero_conta += 1
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da conta: {conta['numero_conta']}")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta Corrente
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato, 
                limite=limite, numero_saques=numero_saques, limite_saques=limite_saques
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF (apenas números): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta_corrente(cpf)

        elif opcao == "q":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Iniciar o sistema
if __name__ == "__main__":
    main()