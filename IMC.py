peso = float(input('Seu peso: (kg)'))
altura = float(input('Sua altura: (m)'))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 25 > imc > 18.5:
    print('Você está no PESO IDEAL.')
elif 30 > imc > 25:
    print('Você está em SOBREPESO.')
elif 40 > imc > 30:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MORBIDA. Cuidado!')
