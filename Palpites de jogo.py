from random import randint
from time import sleep

megasena = '\033[33mMEGA SENA\033[m'
print('-'*30)
print(f'{megasena:^30}')
print('-'*30)
palpites = int(input('Quantos palpites você deseja?: \033[33m'))
print(f'SIMULANDO {palpites} PALPITES...')
sleep(1)
print('\033[m='*30)

num = list()
all = list()
for c in range(0, palpites):
    print(f'\033[33mJOGO {c + 1}: ', end='')
    for p in range(0, 6):
        num.append(randint(0, 60))
        while True:
            if num.count(num[p]) >= 2:
                num.remove(num[p])
                num.append(randint(0, 60))
            else:
                break
    num.sort()
    all.append(num[:])
    print(all[c])
    num.clear()
    sleep(1)
print('\033[mFinalizando...')
sleep(3)
