meses = {
    1: 'Janeiro',
    2: 'Fervereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
    }
mes = int(input('insira um número entre 1 e 12: '))
if mes in meses:
  print(meses[mes])
else:
  print('Número inválido, tente novamente: ')
