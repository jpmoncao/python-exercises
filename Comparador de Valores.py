import os
from time import sleep

while True:
    numeros = list()
    cont2 = ultimo = maior = menor = cont1 = 0
    for c in range(0,5):
        numeros.append(int(input(f'Digite um número para a {c + 1}° posição: ')))
        if c == 0:
            menor = maior = numeros[c]
        else:
            if numeros[c] < menor:
                menor = numeros[c]
            if numeros[c] > maior:
                maior = numeros[c]
    print('Os números digitados foram: ')
    for n in numeros:
            print(f'{n} - ', end='')
    print('')
    print('-='*30)
    print(f'O maior número foi: {maior}\nNa ', end='')
    for c in numeros:
        if c == maior:
            cont1 += 1
    for i, p in enumerate(numeros):
        if p == maior:
            if cont1 >= 2:
                if cont2 == numeros.count(maior)-1:
                    print(f'{i + 1}° posições.')                 
                else:
                    print(f'{i + 1}°, ', end='')
                    cont2 += 1
            else:
                print(f'{i + 1}° posição.')
    cont2 = i = p = ultimo = cont1 = 0
    print(f'E o menor número foi: {menor}\nNa ', end='')
    for c in numeros:
        if c == menor:
            cont1 += 1
    for i, p in enumerate(numeros):
        if p == menor:
            if cont1 >= 2:
                if cont2 == numeros.count(menor)-1:
                    print(f'{i + 1}° posições.')                 
                else:
                    print(f'{i + 1}°, ', end='')
                    cont2 += 1
            else:
                print(f'{i + 1}° posição.')
    print('-='*30)
    resp1 = ' '
    while resp1[0] not in 'SsNn':
        resp1 = input('Deseja inserir outros numeros?[S/N]: ').strip()
    if resp1[0].upper() in 'N':
        print('Finalizando...')
        sleep(2)
        break
    elif resp1[0].upper() in 'S':
        sleep(1)
        os.system('cls')
        cont2 = i = p = ultimo = cont1 = 0   
