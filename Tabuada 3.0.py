from time import sleep
cabeçalho = '-=-'
print(cabeçalho * 20)
numero = int(input('Digite um número para ver a sua tabuada: '))
sleep(1)
while True:
    if numero < 0:
        break
    for fator in range (1,11):
        print(f'{numero} x {fator:2} = {numero * fator}')
    print(cabeçalho * 20)
    numero = int(input('Digite outro número: '))
    sleep(1)
print('Finalizando...')
sleep(1)