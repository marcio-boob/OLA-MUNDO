#CADASTRO DE TRABALHAD
def cadastro_do_trabalhador():

    while True:
        try:
            quantidades = int(input('Informe a quantidades de pessoas: '))
            if quantidades == 0:
              print('Programa encerrado')
              break
            lista = []
            ano_atual = 2026
        except ValueError:
            print('Digite um número valido')
        else:
           for x in range(1,quantidades+1):
            cadastro = {}
            while True:
             cadastro['nome'] = str(input('Digite seu nome: '))
             if cadastro['nome'].isalpha():
                break
             else:
              print('Erro, digite apenas letras')
            
            while True:
                try:
                  ano_nascimento = int(input('Digite seu ano de Nascimento: '))
                  idade = ano_atual-ano_nascimento
                  cadastro['idade'] = idade
                  ctps = int(input('Carteira de trabalho: '))
                  if ctps == 0:
                   cadastro['ctps'] = ctps
                   lista.append(cadastro)
                   print(lista)
                   break
                  else:
                     cadastro['ctps'] = ctps
                     cadastro['ano_contratacao'] = int(input('Ano da Contratação: '))
                     cadastro['salario'] = int(input('Valor do Salário: '))
                     idade = (idade + 35) - (ano_atual - cadastro['ano_contratacao'])
                     cadastro['aposentadoria'] = idade
                     lista.append(cadastro)
                     print(lista)
                     break
                except ValueError:
                  print('Digite uma idade Valida')
    return lista

def lista_cadastro():
    aux = cadastro_do_trabalhador()
    for z,x in enumerate(aux):
       print("\n")
       print(z+1,'Cadastro')
       for valor,t in x.items():
        print(valor,t)
    print("Cadastro Encerrado")
lista_cadastro()
