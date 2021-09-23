print('='*10,'CONVERSOR DE MEDIDA','='*10)
metros = float(input('DIGITE A DISTANCIA EM METROS:'))
print('{} metros(m) é igual a:\n{:.0f} centímetros(cm)\n{:.0f} milímetros(mm)'.format(metros, (metros*100), (metros*1000)))
