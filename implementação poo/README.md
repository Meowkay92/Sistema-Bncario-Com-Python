# Sistema Bancário - Bootcamp NTT DATA DIO

Este projeto foi desenvolvido como parte do Bootcamp NTT DATA da plataforma Digital Innovation One (DIO). O objetivo é implementar um sistema bancário simplificado, seguindo as boas práticas de programação orientada a objetos.

## Descrição

O sistema simula operações bancárias básicas como depósitos, saques e exibição de extratos, além de permitir a criação de usuários e contas correntes. Diferente da implementação anterior que usava dicionários, o sistema agora utiliza classes para melhor modularização e manutenção do código. A estrutura segue o diagrama UML fornecido, utilizando classes como `Cliente`, `Conta`, `Transacao`, e suas subclasses.

## Funcionalidades

- Criar usuários (pessoas físicas) com CPF, nome, data de nascimento e endereço.
- Criar contas correntes vinculadas a um cliente, com controle de saldo, limite de saque diário e histórico de transações.
- Realizar depósitos e saques, validando saldo, limite e quantidade de saques permitidos.
- Exibir extrato de transações da conta.

## Mudanças na Implementação

A implementação foi completamente refatorada para seguir o paradigma de programação orientada a objetos (POO). As principais mudanças são:

1. **Classes**:
   - **`Cliente`**: Representa um cliente que pode ter uma ou mais contas. A classe `PessoaFisica` estende `Cliente` para incluir CPF, nome e data de nascimento.
   - **`Conta`**: Armazena o saldo e permite realizar operações de saque e depósito. A `ContaCorrente` estende essa classe, adicionando limite de saque e controle de número de saques diários.
   - **`Transacao` (Interface)**: Define a interface para operações de depósito e saque. Cada transação pode ser registrada no histórico da conta.
   - **`Historico`**: Armazena as transações realizadas por uma conta.
   
2. **Histórico de Transações**: O histórico de cada conta é registrado na classe `Historico`, que mantém todas as operações realizadas em uma lista de transações.

3. **Transações**:
   - **Depósito**: Aumenta o saldo da conta e registra a transação.
   - **Saque**: Reduz o saldo da conta, desde que haja saldo suficiente, e respeita o limite diário de saques e o valor máximo permitido.

## Como Executar

1. Clone este repositório.
2. Execute o arquivo `main.py` para iniciar o sistema.
3. Utilize o menu interativo para realizar as operações bancárias.

```bash
python main.py
