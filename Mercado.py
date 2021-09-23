total = mais_mil = barato_1 = barato_2 = cont = 0
cabecalho = '-'
print(cabecalho*39 + '\n        SUPERMERCADOS SAKASHITA')
while True:
    print(cabecalho*39)
    nome = str(input('Nome do produto: ')).capitalize()
    valor = float(input('Valor do produto: '))
    total += valor
    if valor > 1000:
        mais_mil += 1
    if cont == 0:
        barato_1 = nome
        barato_2 = valor
    elif cont >= 1 and valor < barato_2:
        barato_1 = nome
        barato_2 = valor
    resposta_1 = ' '
    cont += 1
    while resposta_1 not in 'SN':
        resposta_1 = str(input('Deseja cadastrar outro produto?[S/N]: ')).strip().upper()[0]
    if resposta_1 == 'N':
        break
print(cabecalho*12 + ' Fim da compra ' + cabecalho*12)
print(f'Total a pagar: R${total:.2f}\n{mais_mil} produtos custam mais de R$ 1000,00.'
    f'\nO produto mais barato é o {barato_1}.\n' + cabecalho * 39)
