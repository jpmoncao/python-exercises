from time import sleep
cabecalho = ('~~-')
while True:
    print(cabecalho*20)
    valor_1 = int(input('Olá para começar insira o 1° valor: '))
    valor_2 = int(input('                          2° valor: '))
    print(cabecalho*20, end='\nEscolha uma das opções:\n   [1] adição\n   [2] subtração\n'
        '   [3] multiplicação\n   [4] divisão\n'
        '   [5] maior\n   [6] escolher outros números\n   [7] sair do programa\n')
    resposta_1 = int(input('   ↪ '))
    print(cabecalho*20)
    if resposta_1 == 1:
        print(f'{valor_1} + {valor_2} = {valor_1 + valor_2}')
        print(f'O resultado da adição de {valor_1} e {valor_2} é {valor_1 + valor_2}.')
    elif resposta_1 == 2:
        resultado = valor_1 - valor_2
        print(f'{valor_1} - {valor_2} = {resultado}')
        print(f'o resultado da subtração entre {valor_1} e {valor_2} é {resultado}.')    
    elif resposta_1 == 3:
        resultado = valor_1 * valor_2
        print(f'{valor_1} x {valor_2} = {resultado}')
        print(f'O resultado da multiplicação entre {valor_1} e {valor_2} é {resultado}.')
    elif resposta_1 == 4:
        resultado = valor_1 / valor_2
        print(f'{valor_1} ÷ {valor_2} = {resultado}')
        print(f'O resultado da divisão entre {valor_1} e {valor_2} é {resultado}.')
    elif resposta_1 == 5:
        if valor_1 > valor_2:
            maior = valor_1
            menor = valor_2
        else:
            maior = valor_2
            menor = valor_1
        print(f'O número {maior} é maior que {menor}.')
    elif resposta_1 == 6:
        continue
    elif resposta_1 == 7:
        print('Finalizando...')
        sleep(2)
        break
    else:
        print('Opção invalida... Tente novamente.')
