lista_de_numeros = []
lista_com_erros = []

for x in range(0,7):
    numero = int(input('Informe um número de 1 a 7: '))
    if numero == 0:
        break
    if numero <= 7:
     lista_de_numeros.append(numero)
    if numero > 7:
       lista_com_erros.append(numero)
       
print('-' * 33)
if lista_de_numeros:
    print(f'Lista com números {lista_de_numeros}')
else:
    print('lista vazia')
    
if lista_com_erros:
    print(f'Lista com erros {lista_com_erros}')
else:
    print('lista com erros vazia')
