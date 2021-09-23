from random import randint
numbers = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
print('Os números que foram sorteados são: ', end='')
cont = 0
for c in numbers:
    if c == numbers[-1]:
        print(f'{c}.')
    else:
        print(f'{c}, ', end='')
print(f'Sendo o maior valor o \033[32m{max(numbers)}\033[m e o menor o \033[33m{min(numbers)}\033[m.')
