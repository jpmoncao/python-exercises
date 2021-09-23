from random import randint
from time import sleep
print('Olá, o computador escolheu um número de 0 a 5... E aí você é capaz de adivinhar qual foi?')
num = int(randint(0,5))
adv = int(input('Adivinhe o número escolhido:'))
print('PROCESSANDO...')
sleep(2)
if adv == num:
    print('Parabéns, você acertou!')
else:
    print('Ops... Você errou. O número que eu pensei foi {}'.format(num))
nov = str(input('Deseja jogar novamente?')).strip().lower()
if nov == 'sim':
    print('LEGAL! Reinicie o código e bora lá...')
else:
    print('Foi mt divertido sua participação até mais!')
print('-'*200)


