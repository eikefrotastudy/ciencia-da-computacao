# TRATAMENTO DE EXCEÇÕES 

# try:
#     num = eval(input("Digite um valor: "))
#     print(num)
# except:
#     print("Digite um valor númerico e não letras")


try:
    num = eval(input("Digte um número: "))
    resultado = 10/num
    print(resultado)
except ZeroDivisionError as error:
    print("Não é possivel dividir por zero!", error)
except NameError:
    print("O valor inserido não é númerico!")