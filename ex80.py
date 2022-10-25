lista = []

cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        cont += 1
        lista.append(n)


    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Sua lista foi com esses valores {lista}')
print(f'vc digitou {len(lista)} valores')
print(f'Sua lista crecente é {sorted(lista)}')
print(f'sua lista decrecente é {sorted(lista, reverse =True)}')
print('O valor 5 esta na lista' if 5 in lista else 'O valor 5 não esta na lista')
    
