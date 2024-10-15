from abc import ABC, abstractmethod


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        conta.realizar_transacao(transacao)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, cpf, data_nascimento, endereco)


class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def exibir_extrato(self):
        print("\n===== Extrato =====")
        for transacao in self.historico.transacoes:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("===================")


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, limite, limite_saques):
        super().__init__(agencia, numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saldo insuficiente com limite.")
            return False
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques atingido.")
            return False
        self.saldo -= valor
        self.numero_saques += 1
        self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


def criar_usuario(usuarios, nome, cpf, data_nascimento, endereco):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Usuário já cadastrado com este CPF.")
            return None

    novo_usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return novo_usuario


def criar_conta_corrente(usuarios, contas, cpf, agencia, numero_conta, limite=500, limite_saques=3):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return None

    nova_conta = ContaCorrente(agencia, numero_conta, usuario_encontrado, limite, limite_saques)
    contas.append(nova_conta)
    usuario_encontrado.adicionar_conta(nova_conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da conta: {numero_conta}")
    return nova_conta


def listar_contas(contas):
    print("\n===== Contas Disponíveis =====")
    for conta in contas:
        print(f"Agência: {conta.agencia} | Número: {conta.numero} | Cliente: {conta.cliente.nome}")
    print("==============================")


def main():
    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1  # Inicia o número da conta em 1

    while True:
        menu = """
        [nu] Novo Usuário
        [nc] Nova Conta Corrente
        [d] Depositar
        [s] Sacar
        [e] Exibir Extrato
        [lc] Listar Contas
        [q] Sair
        => """

        opcao = input(menu)

        if opcao == "nu":
            nome = input("Informe o nome: ")
            cpf = input("Informe o CPF: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Informe o endereço: ")
            criar_usuario(usuarios, nome, cpf, data_nascimento, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do usuário: ")
            nova_conta = criar_conta_corrente(usuarios, contas, cpf, agencia, numero_conta)
            if nova_conta:
                numero_conta += 1  # Incrementa o número da conta para a próxima

        elif opcao == "d":
            listar_contas(contas)
            numero_conta_input = int(input("Informe o número da conta para depósito: "))
            valor = float(input("Informe o valor do depósito: "))
            conta = next((conta for conta in contas if conta.numero == numero_conta_input), None)
            if conta:
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            listar_contas(contas)
            numero_conta_input = int(input("Informe o número da conta para saque: "))
            valor = float(input("Informe o valor do saque: "))
            conta = next((conta for conta in contas if conta.numero == numero_conta_input), None)
            if conta:
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "e":
            listar_contas(contas)
            numero_conta_input = int(input("Informe o número da conta para exibir o extrato: "))
            conta = next((conta for conta in contas if conta.numero == numero_conta_input), None)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
