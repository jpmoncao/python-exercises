cont = 0
print('\033[32m-' * 5, 'Tabuada', '-' * 5)
num = int(input('Escolha um número: '))
print('-' * 15)
for c in range(0, 10):
    print('\033[32m{}\033[m  x {:2} = {}'.format(num, c + 1, num * (c + 1)))
print('\033[32m-' * 15)
