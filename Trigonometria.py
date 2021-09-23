import math
ang = float(input('Digite um ângulo:'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo {} tem o SENO de {:2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(ang,seno,cos,tang))