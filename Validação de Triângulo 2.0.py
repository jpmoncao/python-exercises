from time import sleep
print('\033[36m='*50)
print(' '*9, '△ ANALISADOR DE TRIÂNGULOS △', ' '*9)
print('='*50)
print('\033[1;4;31mInsira três segmentos abaixo, e o código fará uma análise da figura.\033[4;36m')
seg1 = int(input('Primeiro segmento:'))
seg2 = int(input('Segundo  segmento:'))
seg3 = int(input('Terceiro segmento:\033[m'))
per = seg1 + seg2 + seg3
if seg1 > seg2+seg3 or seg2 > seg1+seg3 or seg3 > seg1+seg2:
    print('\033[0;31mERRO!\033[m Não é possivel formar um triângulo com esses 3 segmentos indicados.'
          '\033[36;1;4m\nPois não segue a condição de existência de um triângulo. Saiba mais em: '
          'https://bityli.com/0nTYW')
else:
    print('Processando...')
    sleep(3)
    if seg1 == seg2 and seg1 == seg3:
        print('Os segmentos indicados formam um triângulo \033[36mEQUILÁTERO!\033[m')
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print('Os segmentos indicados formam um triângulo \033[36mESCALENO!\033[m')
    else:
        print('Os segmentos indicados formam um triângulo \033[36mISÓSCELES!\033[m')
    print('Seu perímetro é de: {}.'.format(per))
    print('\033[36;1;4mVocê viu uma palavra e não sabe seu significado?\033[m \n\033[34;1mDigite "Vocabulario" para '
          'acessar o seu '
          'significado.\nPressione Enter para sair\nOu Ctrl+F5 para reinicializar')
    resp1 = str(input('⇒'))
    if resp1.isalpha():
        print('\033[36mVOCABULÁRIO')
        print('\033[36;1m  SEGMENTO:\033[m Numa reta ou curva, a porção limitada por dois pontos.')
        print('\033[36;1m TRIÂNGULO:\033[m Polígono de três lados e três ângulos. (A área de um triângulo é igual à '
              'metade do produto de sua base pela altura).')
        print('\033[36;1mEQUILÁTERO:\033[m Figura que possui todos os lados ou faces iguais.')
        print('\033[36;1m  ESCALENO:\033[m Triângulo cujos lados e ângulos são todos desiguais.')
        print('\033[36;1m ISÓSCELES:\033[m Figura que possui apenas dois lados iguais.')
    else:
        print('\033[36;1m-'*120)
    # Futuramente voltar no projeto para deixar mais complexo - print('Sua área é de {}...'.format(area))
