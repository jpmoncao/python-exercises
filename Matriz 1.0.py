matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for h in range(0,3):
    for v in range(0, 3):
        matriz[h][v] = int(input(f'Digite um número para a posição [{h}, {v}]: '))
for h in range(0, 3):
    for v in range(0, 3):
        if v != 2:
            print(f'[{matriz[h][v]:^5}] ', end='')
        else:
            print(f'[{matriz[h][v]:^5}]')
