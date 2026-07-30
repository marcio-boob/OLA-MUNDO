def menu():
    lista1 = ['inserir','retirar']
    print('LISTA DE OPÇÕES:')
    print("\n")
    for cont,item in enumerate(lista1):
        print(f'{cont+1} opção {item}')
    print("\n")
    return lista1

def opcoes(lista1):
    while True:
        opcao = str(input('Escolha uma das  opções. Para sair digite [não]: ')).lower().strip()
        if opcao == 'não':
         print('Programa encerrado')
         break
        
        
        if opcao == '':
            print('invalido')
        
        if opcao in lista1:
           return opcao

lista1=menu()
lista = []

def inserir_elementos():
     retorno=opcoes(lista1)
     while retorno == 'inserir':
      inserir = str(input('Insira um item: '))
      if inserir == 'não':
        break
      
      
      elif inserir == '':
         print('Invalido')
         continue

      elif inserir  in lista:
         print('Item já está na lista')
         continue
   
      lista.append(inserir)
     return lista

inserir_elementos()

def lista_dos_elementos():
    if lista:
        print("\nIntens da lista:")
        for cont,x in enumerate(lista):
         print(f'{cont+1}ª item {x}')
    return lista
lista_dos_elementos()

def retirar_itens():
    
    if lista:
     while True:
       retirar = str(input('retirar itens da lista ? '))
       if retirar == '':
          print('Entrada vazia')
          continue
       elif retirar == 'não':
          print('Programa encerrado')
          break
       elif retirar not in lista:
         print('Não está na lista')
       else:
          lista.remove(retirar)
          print("\nLista dos itens")
          for cont,p in enumerate(lista):
            print(f'{cont+1} item {p}')

     return lista
     
retirar_itens()