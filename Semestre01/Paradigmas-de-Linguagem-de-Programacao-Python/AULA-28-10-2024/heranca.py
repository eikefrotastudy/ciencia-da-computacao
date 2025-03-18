class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    def info(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSalário: R${self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_gerenciados = qtd_gerenciados
    
    def info(self):
        info = super().info()
        return f"{info}\nQuantidade de Gerenciados: {self.qtd_gerenciados}"

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, duracao_estagio):
        super().__init__(nome, cpf, salario)
        self.duracao_estagio = duracao_estagio
    
    def info(self):
        info = super().info()
        return f"{info}\nDuração do Estágio: {self.duracao_estagio} meses"

funcionario1 = Funcionario("Enzo", "604.133.373-59", 3000)
gerente1 = Gerente("Eike", "604.133.243-70", 5000, "1234", 10)
estagiario1 = Estagiario("Mariana", "123.456.789-10", 1500, 6)

print(funcionario1.info())
print(gerente1.info())
print(estagiario1.info())
