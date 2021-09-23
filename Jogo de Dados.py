from random import randint
jogadores = dict()
lista = list()
for c in range(0, 4):
    jogadores['nome'] = input(f'{c + 1}° jogador: ')
    input('Pressione \033[36m"ENTER"\033[m para jogar o dado.')
    jogadores['dado'] = randint(1, 6)
    lista.append(jogadores.copy())
    print(f'O {jogadores["nome"]} jogou o dado em {jogadores["dado"]}!')
print(jogadores['dado'].sort())

