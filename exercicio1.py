#CADASTRO DE TRABALHAD
def cadastro_do_trabalhador():

    while True:
        try:
            quantidades = int(input('Informe a quantidades de pessoas: '))
            if quantidades == 0:
              print('Programa encerrado')
              break
            lista = []
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
                 cadastro['idade'] = int(input('Digite sua idade: '))
                 break
                except ValueError:
                 print('Digite uma idade valida')
                 
                
            

cadastro_do_trabalhador()

