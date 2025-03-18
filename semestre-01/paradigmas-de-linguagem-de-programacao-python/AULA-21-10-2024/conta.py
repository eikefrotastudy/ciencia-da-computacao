class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito efetuado com sucesso!")
    
    def gerar_extrato(self):
        print(f"Número: {self.numero}\nCPF: {self.cpf}\nNome do Titular: {self.nomeTitular}\nSaldo: {self.saldo}")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print("Saque efetuado com sucesso!")


conta1 = Conta(1, '123.456.789.10', 'João', 1000)

conta1.depositar(500)
conta1.gerar_extrato()
conta1.sacar(250)

print(f"O saldo é {conta1.saldo}")


        