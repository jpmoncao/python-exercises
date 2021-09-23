import math
print('-'*25, 'TEOREMA DE PITAGORAS', '-'*25)
a = float(input('Comprimento do cateto oposto:'))
b = float(input('Comprimento do cateto adjacente:'))
c = math.hypot(a, b)
print ('O valor da hipotenusa é igual a {:.2f}!'.format(c))
