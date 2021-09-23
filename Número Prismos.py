from time import sleep
while True:
    # Cabeçalho
    cabeçalho = '='
    print(cabeçalho *20,
        'Números primos',
        cabeçalho *20)

    num = int(input('Digite um número:'))
    mult = 0
    for cont in range(2, num-1):
        if num % cont == 0:
            mult += 1
    if mult == 0:
        cond = 'é'
    else:
        cond = 'não é'
    print('\n\033[m', cabeçalho*56)
    print(f'O número {num}, {cond} um número primo.')
    print(cabeçalho*56)
    print('\n\033[mDeseja reiniciar? s/n')
    r = input('Sua opção ⇒ ')
    if r == 'n':
        break
    elif r == 's':
        sleep(2)
        continue
