reta1 = int(input('Primeiro segmento:'))
reta2 = int(input('Segundo segmento:'))
reta3 = int(input('Terceiro segmento:'))
sim = 1
if reta1>reta2+reta3:
    sim = 0
if reta2>reta1+reta3:
    sim = 0
if reta3>reta1+reta2:
    sim = 0
if sim == 1:
    print('SIM, é possivel formar um triângulo!')
else:
    print('NÃO é possível formar um triângulo!')