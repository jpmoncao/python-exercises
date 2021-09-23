soma = segunda = terceira = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for h in range(0, 3):
    for v in range(0, 3):
        matriz[h][v] = int(input(f'Digite um número para posição [{h}, {v}]: '))
for h in range(0, 3):
    for v in range(0, 3):
        if h == 1:
            if v == 0:
                segunda = matriz[h][v]
            else:
                if segunda < matriz[h][v]:
                    segunda = matriz[h][v]
        if v == 2:
            print(f'[{matriz[h][v]:^3}]')
            terceira += matriz[h][v]
        else:
            print(f'[{matriz[h][v]:^3}]', end='')
        soma += matriz[h][v]
print(f'Soma dos valores: {soma}\n'
    f'Soma dos valores 3ª coluna: {terceira}\n'
    f'Maior valor da 2ª linha: {segunda}')
