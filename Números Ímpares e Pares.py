numeros = list()
pares = list()
impares = list()
resp1 = ' '
while resp1[0].upper() not in 'N':
    numeros.append(int(input('Digite um número: ')))
    if numeros[-1] % 2 == 0:
        pares.append(numeros[-1])
    else:
        impares.append(numeros[-1])
    resp1 = input('Deseja inserir outro número?[S/N]: ').strip()
print('Os números digitados foram:', end='')
for c in numeros:
    if c == numeros[-1]:
        print(f'{c}.')
    else:
        print(f'{c} - ', end='')
if len(pares) == 0 and len(impares) > 0:
    print('Sendo ', end='')
    for c in impares:
        if c == impares[-1] and len(pares)  > 1:
            print(f'{c} ímpares.')
        elif len(impares) == 1:
            print(f'{c} ímpar.') 
        else:
            print(f'{c}, ', end='')
    print('Nenhum número par foi digitado')
elif len(impares) == 0 and len(pares) > 0:
    print('Sendo ', end='')
    for c in pares:
        if c == pares[-1] and len(pares) > 1:
            print(f'{c} pares.')
        elif len(pares) == 1:
            print(f'{c} par.') 
        else:
            print(f'{c}, ', end='')
    print('Nenhum número ímpar foi digitado')
elif len(pares) > 0 and len(impares) > 0:
    print('Sendo ', end='')
    for c in pares:
        if c == pares[-1] and len(pares) > 1:
            print(f'{c} pares.')
        elif len(pares) == 1:
            print(f'{c} par.')  
        else:
            print(f'{c}, ', end='')
    print('E ', end='')
    for c in impares:
        if c == impares[-1] and len(pares) > 1:
            print(f'{c} ímpares.') 
        elif len(impares) == 1:
            print(f'{c} ímpar.') 
        else:
            print(f'{c}, ', end='')
