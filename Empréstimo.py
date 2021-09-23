# Importações
from time import sleep

# Apresentação
print('\033[31m-=-\033[m' * 50)
print('\033[1;31;40mCOLOQUE OS DADOS NECESSARIOS PARA CRIAR O ORÇAMENTO E CONFIRA SE SERA POSSIVEL A OPERAÇÃO...')
print('\033[m\033[31m-=-\033[m' * 50)

# Variáveis
val = float(input('\033[1mQual o valor do empréstimo?: R$'))
sal = float(input('Qual é o seu salário?: R$'))
sal30 = (sal * 30) / 100
anos = int(input('Em quantos anos você deseja pagar?:'))

if anos <= 0:
    print('\033[31mEMPRÉSTIMO NEGADO, POIS O VALOR DIGITADO FOI MENOR QUE O MÍNIMO DE 1 ANO.')
else:
    valf = val / (anos * 12)
    if valf <= sal30:
        print('O emprestimo de R${:.2f} em {} anos foi \033[1;32mAPROVADO\033[m,'.format(val, anos), end='')
        print('avaliado em R${:.2f} por mês.'.format(valf))
        print('Consulte a nossa operadora mais próxima para continuar!')
        print('\033[1;31mDigite "sim ou "não"\033[m')
        resp = str(input('Deseja ver a localização da nossa operadora mais próxima?:')).strip().lower()
        if resp == 'sim':
            print('\033[4;31mPROCESSANDO...')
            sleep(3)
            print('\033[mFica localizada na rua Irineu, você não sabe nem eu kdakskdsakdka!')
    else:
        print('O emprestimo foi \033[1;31mNEGADO\033[m pois R${:.2f}'.format(valf), end='')
        print('por mês excede os 30% permitido no seu orçamento!')
print('\033[mTenha um bom-dia!')
