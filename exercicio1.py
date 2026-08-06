#CADASTRO DE TRABALHADORR
def cadastro_do_trabalhador():
    quantidades = int(input('Informe a quantidades de pessoas: '))
    lista = []
    for x in range(1,quantidades+1):
        cadastro = {}
        cadastro['nome'] = str(input('Digite seu nome: '))
        cadastro['idade'] = int(input('Digite sua idade: '))
        lista.append(cadastro)
    print(lista)
    return lista
cadastro_do_trabalhador()
