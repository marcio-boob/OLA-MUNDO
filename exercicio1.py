#CADASTRO DE TRABALHADORR
lista = []
while True:
    cadastro = {}
    cadastro['nome'] = str(input('Digite seu nome:'))
    cadastro['idade'] = int(input('Digite sua idade'))
    lista.append(cadastro)
    print(lista)
