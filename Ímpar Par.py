from random import randint
from time import sleep

cabecalho = '↢↣'
par = impar = 0
print(cabecalho * 30)
print('Bem vindo ao ímpar ou par! Para começar...')
while True:
    escolha_jogador = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    if escolha_jogador in 'P':
        par = True
        impar = False
    elif escolha_jogador in 'IÍ':
        par = False
        impar = True
    else:
        break
    print(cabecalho * 30)
    numero_jogador = int(input('Ok, agora escolha um número de 0 a 10: '))
    numero_computador = randint(1,10)
    resultado = numero_computador + numero_jogador
    if resultado % 2 == 0:
        p_ou_i = 'PAR'
        if par is True:
            win = 'GANHOU'
        else:
            win = 'PERDEU'
    elif resultado % 2 != 0:
        p_ou_i = 'ÍMPAR'
        if impar is True:
            win = 'GANHOU'
        else:
            win = 'PERDEU'
    print('3...\n2...\n1!')
    print(cabecalho*30, f'\nVOCÊ {win}!\nVocê digitou {numero_jogador} e o computador {numero_computador},'
        f' dando um total de {resultado}. QUE É {p_ou_i}')
    print(cabecalho*30)
    if win == 'PERDEU':
        break
sleep(2)
print('Finalizando...')
sleep(1)
