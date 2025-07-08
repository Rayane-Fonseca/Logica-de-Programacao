class ContaBancaria:

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print (f"Depósito de R${valor:.2f}")

        else:
            print("Valor de deposito inválido!")

    def sacar(self, valor):

        #valor = input ("Digite o valor que deseja sacar: ")

        if valor < self.saldo:
            self.saldo -= valor
            print (f"Saque no valor de R${valor:.2f} realizado!")

        else:
            print("Valor de saque inválido!")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}") #2f para limitar o valor depois da virgula: ,00

conta = ContaBancaria("Rayane", 1000)
conta.consultar_saldo()
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()