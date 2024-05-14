from abc import ABC

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def criar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self. data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = ""
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso ===")
        else:
            print("\nNão foi possível realizar o depósito! O valor informado é inválido")
            return False
        return True
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_limite = valor > saldo

        if excedeu_limite:
            print("\n=== Não foi possível realizar o saque! Saldo insuficiente. ===")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso ===")
            return True        
        else:
            print("\nO valor informado é inválido.")
        
        return False
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques