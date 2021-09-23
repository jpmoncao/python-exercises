titulo = 'BANCO CEV'
print('==='*15)
print('\033[32m' + titulo.center(45) + '\033[m')
print('==='*15)
valor = int(input('Qual valor será sacado? R$'))
total = valor
céd = 100
totcéd = 0
print('==='*15)
print('\033[32mVocê receberá:\033[m ')
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd:.2f}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('==='*15)
print('Obrigado pela preferência, \nvolte sempre ao banco Curso em vídeo!')
print('==='*15)
