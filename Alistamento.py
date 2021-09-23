# Importações
from datetime import date

# Variáveis
nome = str(input('Nome completo:')).strip().title()
sexo = str(input('Sexualidade:')).strip().lower()
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano
falta = 18 - idade
passou = idade - 18
anosf = 18 - idade + atual
anosp = atual - (idade - 18)

if sexo == 'feminino' or sexo == 'mulher' or sexo == 'menina':
    print('Responda com "Sim" ou "Não"')
    resp = str(input('O alistamento para mulheres não é obrigatório deseja continuar?'))
    if resp == 'não' or resp == 'nao':
        print('Ok, tenha um bom dia.')
    else:
        print('Olá {}.\nVocê nasceu em \033[36m{} e tem {} anos.\033[m'.format(nome, ano, idade))
        if idade == 18:
            print('\033[1mVocê deve se alistar ainda esse ano!\nFique atento e se aliste o mais rápido possivel...')
        elif idade < 18:
            print('Ainda falta \033[36m{} anos\033[m para você se alistar, fique atento!'.format(falta))
            print('Seu alistamento será em {}'.format(anosf))
        elif idade > 18:
            print('Ja se passou \033[36m{} anos\033[m da data correspondente ao seu alistamento.'.format(passou))
            print('Seu alistamento foi em {}!'.format(anosp))
elif sexo != 'feminino' or sexo != 'mulher' or sexo != 'menina':
    print('Olá {}.\nVocê nasceu em \033[36m{} e tem {} anos.\033[m'.format(nome, ano, idade))
    if idade == 18:
        print('\033[1mVocê deve se alistar ainda esse ano!\nFique atento e se aliste o mais rápido possivel...')
    elif idade < 18:
        print('Ainda falta \033[36m{} anos\033[m para você se alistar, fique atento!'.format(falta))
        print('Seu alistamento será em {}'.format(anosf))
    elif idade > 18:
        print('Ja se passou \033[36m{} anos\033[m da data correspondente ao seu alistamento.'.format(passou))
        print('Seu alistamento foi em {}!'.format(anosp))
