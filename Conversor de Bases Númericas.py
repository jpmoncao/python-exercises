print('\033[36m-=-'*20)
print(' '*15, 'CONVERSOR DE BASES NÚMERICAS')
print('\033[36m-=-\033[m'*20)
num = int(input('Insira um número:'))
print('Você deseja convertê-lo para:')
print('\033[36m [ 1 ] \033[m converter para \033[36mHEXADECIMAL\033[m')
print('\033[36m [ 2 ] \033[m converter para \033[36mBINÁRIO    \033[m')
print('\033[36m [ 3 ] \033[m converter para \033[36mOCTAL      \033[m')
opc = int(input('\033[4mSua opção:\033[m'))
if opc == 1:
    print('{} convertido em HEXADECIMAL é igual a {}!'.format(num, hex(num)[2:]))
elif opc == 2:
    print('{} convertido em BINÁRIO é igual a {}!'.format(num, bin(num)[2:]))
elif opc == 3:
    print('{} convertido em OCTAL é igual a {}!'.format(num, oct(num)[2:]))
else:
    print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
