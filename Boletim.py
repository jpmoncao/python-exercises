from time import sleep
from os import system

resp1 = resp2 = ' '
find = cont1 = 0
lista = []
aluno = []
print('\033[1;35m-----------BOLETIM-----------\033[m')
while True:
    while resp1[0].upper() not in 'N':
        aluno.append(input('\033[36mNome: \033[m'))
        for c in range(0, 2):
            aluno.append(float(input(f'\033[36mNota {c + 1}: \033[m')))
        lista.append(aluno[:])
        aluno.clear()
        resp1 = input('Deseja continuar?[S/N]: \033[36m')
    if cont1 < 1:
        print('\033[m=-'*30)
        print('\033[36m|N°   Nome              Média|')
        for c in range(len(lista)):
            print(f'\033[m {c:^2} {lista[c][0]:^15}    \033[36m{(lista[c][1] + lista[c][2]) / 2:^5}\033[m')
        cont1 += 1
    print('=-'*30)
    print('\033[35m[0]\033[m Filtrar por notas individuais\n\033[35m[1]\033[m Reiniciar\n\033[35m[2]\033[m Finalizar')
    while resp2 not in '012':
        resp2 = input('\033[35m>>> ')
    print('\033[m=-'*30)
    if resp2[0] in '0':
        find = int(input('Número do aluno: '))
        print(f'{lista[find][0]}: {lista[find][1:]}')
        sleep(2)
    elif resp2[0] in '2':
        break
    else:
        cont1 = 0
        resp1 = ' '
        lista.clear()
        system('cls')
        print('\033[1;35m-----------BOLETIM-----------\033[m')
    resp2 = ' '
print('Finalizando...')
sleep(1)
