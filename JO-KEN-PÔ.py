# Importações
from time import sleep
from random import randint

# Enunciado
print('\033[1;36m=' * 40)
print('{:=^40}'.format('BEM-VINDO AO JO-KEN-PO!:THE GAME'))
print('{:=^40}'.format('ENJOY =)'))
print('=' * 40)
print('\033[36;3mPara começar, primeiro escolha uma das\033[m\n\033[36;3;1mtrês opções abaixo,'
      'e descubra se você\033[m\n\033[36;3;1mé bom o bastante para vencer o computador💻.\033[m')

# Escolha
print('\n\033[36;1mEscolha sua jogada\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
jogador = int(input('Qual a sua jogada ⇒ '))

# Conversão
if jogador == 1:
    jogador = 0
elif jogador == 2:
    jogador = 1
elif jogador == 3:
    jogador = 2

# Varíaveis
lista = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
condicao = ''

# Opção inválida
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[31mEssa jogada não existe, tente novamente.')

# Condições de vitória e derrota
else:
    if comp == 0:  # Computador escolhe 1 - PEDRA
        if jogador == 0:
            condicao = '\033[33mEMPATE\033[m'
        elif jogador == 1:
            condicao = '\033[32mVITÓRIA\033[m'
        elif jogador == 2:
            condicao = '\033[31mDERROTA\033[m'
    elif comp == 1:  # Computador escolhe 2 - PAPEL
        if jogador == 0:
            condicao = '\033[31mDERROTA\033[m'
        elif jogador == 1:
            condicao = '\033[32mEMPATE\033[m'
        elif jogador == 2:
            condicao = '\033[32mVITÓRIA\033[m'
    elif comp == 2:  # Computador escolhe 3 - TESOURA
        if jogador == 0:
            condicao = '\033[32mVITÓRIA\033[m'
        elif jogador == 1:
            condicao = '\033[31mDERROTA\033[m'
        elif jogador == 2:
            condicao = '\033[33mEMPATE\033[m'
    print('JO')
    sleep(1)
    print('KEN')
    sleep(0.5)
    print('PÔ!')

    # Resultado final
    print(condicao)
    print('Você escolheu \033[36m{}\033[m e o computador escolheu '
          '\033[36m{}\033[m!'.format(lista[jogador], lista[comp]))
print('\033[36mCtrl+F5 para jogar novamente!')
