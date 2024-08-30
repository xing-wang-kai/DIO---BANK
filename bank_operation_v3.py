from abc import ABC, abstractmethod
from datetime import date

# Interface para transações
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: 'Conta'):
        pass

# Classe de Histórico para armazenar transações
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

# Classe principal Conta
class Conta:
    def __init__(self, cliente: 'Cliente', numero: int, agencia: str, saldo: float = 0.0):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self) -> float:
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente: 'Cliente', numero: int, agencia: str) -> 'Conta':
        return cls(cliente, numero, agencia)

    def sacar(self, valor: float) -> bool:
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            return True
        return False

# Classe de Conta Corrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, cliente: 'Cliente', numero: int, agencia: str, saldo: float = 0.0, limite: float = 1000.0, limite_saques: int = 3):
        super().__init__(cliente, numero, agencia, saldo)
        self.limite = limite
        self.limite_saques = limite_saques

# Classe para Depósito
class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso.")
        else:
            print("Depósito falhou.")

# Classe para Saque
class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso.")
        else:
            print("Saque falhou. Verifique o saldo ou limite.")

# Classe para Cliente
class Cliente:
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

# Classe para Pessoa Física
class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(cpf, nome, data_nascimento, endereco)

# Função para exibir o menu e realizar as operações
def menu():
    print("""
    Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [lt] Listar Contas
    [q] Sair
    """)
    return input().lower()

def main():
    contas = []
    usuarios = []
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 'd':
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                valor = float(input("Informe o valor para depósito: "))
                conta = usuario.contas[0]
                deposito = Deposito(valor)
                usuario.realizar_transacao(conta, deposito)
            else:
                print("Usuário não encontrado.")

        elif opcao == 's':
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                valor = float(input("Informe o valor para saque: "))
                conta = usuario.contas[0]
                saque = Saque(valor)
                usuario.realizar_transacao(conta, saque)
            else:
                print("Usuário não encontrado.")

        elif opcao == 'e':
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                conta = usuario.contas[0]
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
                print("Extrato:")
                for transacao in conta.historico.transacoes:
                    print(f"- {type(transacao).__name__} no valor de R$ {transacao.valor:.2f}")
            else:
                print("Usuário não encontrado.")

        elif opcao == 'nc':
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                numero_conta = len(contas) + 1
                conta = ContaCorrente(cliente=usuario, numero=numero_conta, agencia=AGENCIA)
                usuario.adicionar_conta(conta)
                contas.append(conta)
                print("Conta criada com sucesso.")
            else:
                print("Usuário não encontrado.")

        elif opcao == 'nu':
            cpf = input("CPF: ")
            nome = input("Nome: ")
            data_nascimento = date.fromisoformat(input("Data de nascimento (YYYY-MM-DD): "))
            endereco = input("Endereço: ")
            usuario = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
            usuarios.append(usuario)
            print("Usuário criado com sucesso.")

        elif opcao == 'lt':
            for conta in contas:
                print(f"Agência: {conta.agencia}, Conta: {conta.numero}, Cliente: {conta.cliente.nome}")

        elif opcao == 'q':
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
