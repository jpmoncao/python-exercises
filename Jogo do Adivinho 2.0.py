from time import sleep
from random import randint
while True:
    numero_certo = int(randint(1,10))
    cont = 0
    acertou = False
    print('=~'*40)
    print('Olá, o computador escolheu um número de 1 a 10. \nE você tem o desafio'
        ' de acertar que número é esse.')
    print('=~'*40)
    numero_escolhido = int(input('Para começar, escolha um número de 1 a 10: '))
    sleep(1)
    while numero_escolhido > 10:
        print('=~'*20)
        print('Ops... Parece que esse número é invalido...')
        numero_escolhido = int(input('Escolha um número de 1 a 10: '))
        sleep(1)
    while not acertou:
        print('=~'*20)
        if numero_escolhido == numero_certo:
            print(f'Parabéns, você acertou. O número correto era o {numero_certo}!')
            acertou = True
        else:
            cont += 1
            if numero_escolhido > numero_certo:
                numero_escolhido = int(input(f'Tente um número menor que {numero_escolhido}: '))
            elif numero_escolhido < numero_certo:
                numero_escolhido = int(input(f'Tente um número maior que {numero_escolhido}: '))
    if cont == 0:
        print('Incrível! Você conseguiu em apenas 1 tentativa!')
    else: 
        print(f'Você precisou de {cont + 1} tentativas para acertar! ')
    print('=~'*20)
    resp = str(input('Quer jogar mais uma vez?[Sim/Não]: ')).strip()[0]
    if resp in 'Ss':
        print('Ótimo!')
        continue
    elif resp in 'Nn':
        print('Ok... Até a próxima! bye =D')
        print('=~'*20)
        break
    else:
        break