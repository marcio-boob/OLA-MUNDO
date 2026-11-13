lista = [['a','b','c'],['h','i','j']]

nome = str(input('Nome do aluno: '))
for cont,x in enumerate(lista):
    
    if nome == lista[cont][0]:
        print('yes')
        break
else:
     print('Not')