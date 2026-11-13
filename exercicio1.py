#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

def cadastro_escolor():
    
    cadastro =[]
    while True:
        try:
           quantidade_de_alunos = int(input('Digite a quantidade de alunos: '))
           print()
           if quantidade_de_alunos == 0:
              break
           
           elif quantidade_de_alunos < 0:
            print('Número negativo não permitido')
           elif quantidade_de_alunos > 10:
            print('Quantidade não permitida.')
           else:

            for _ in range(1,quantidade_de_alunos+1):
               notas = []

               while True:
                 nome = str(input('Digite seu nome: ')).title()
                 if not nome.replace(' ', '').isalpha():
                  print('Erro!')
                 else:
                  break
  
               while True:
  
                    try:
                       quantidade_de_notas = int(input('Quantidade das notas: '))
                       for _ in range(1,quantidade_de_notas+1):
                        while True:
                            try:
                              nota = int(input('Digite sua nota: '))
                              notas.append(nota)
                              break
                            except ValueError:
                             print('Digite um número valido')  
                       media = sum(notas) / len(notas) 
                       cadastro.append([nome,notas,media]) 
                       break
                    except ValueError:
                     print('Digite um número valido YES')
                            
        except ValueError:
         print('Digite um número valido')     
    return cadastro


def lista_de_cadastro():
   aux = cadastro_escolor()
   # print(aux)

   if not aux:
     print('Lista vazia')
   else:
    print(f"{'Nome':<11} {'Notas':<11} {'Média'}")
    for x in aux:
       
       print(f'{str(x[0]):<10}  {str(x[1]):<10}  {x[2]:.2f}')

    print()   

    while True: 
     nome = str(input('Nome do aluno: ')).title()
     if nome == 'sair'.title():
       break
     else:
      if not  nome.replace(' ', '').isalpha():
       print('erro')
       continue
     
     for cont,f in enumerate(aux):
       if nome in aux[cont][0]:
   
        print(f'{str(f[0]):<10}  {str(f[1]):<10}  {f[2]:.2f}')                                  
        break

     else:
        print('not')
       
   
lista_de_cadastro()