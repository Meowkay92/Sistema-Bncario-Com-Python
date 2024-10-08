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


