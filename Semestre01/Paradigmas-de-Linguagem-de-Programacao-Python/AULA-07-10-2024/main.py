def mostrar_mensagem():
    print("Sistema de Impressão v.1.0")

# for i in range(5):
#     mostrar_mensagem()

def assinar(nome, email):
    print("Atenciosamente, ")
    print(f"Prof. {nome}")
    print(email)

# assinar("Eike Frota", "eikefrota@gmail.com")

def area_circulo(r):
    area = 3.141592 * r**2
    return area

# a = area_circulo(2)
# print(f"A área do circulo é: {a}")

def leitura_de_nome():
    nome = input("Por favor, digite seu nome: ")
    sobrenome = input("Por favor, digite seu sobrenome: ")
    nome_completo = nome + " " + sobrenome
    return nome_completo

# usuario = leitura_de_nome()
# print(f"Bom dia, {usuario}!")

def calculo_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc01 = calculo_imc(peso, altura)

print(f"Seu IMC é: {imc01}")