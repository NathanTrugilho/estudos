data = input('Informe a data de nascimento no formato (dd/mm/aaaa): ')

mes = data[3:5]

if mes == '01':
    mes = 'Janeiro'

elif mes == '02':
    mes = 'Fevereiro'

elif mes == '03':
    mes = 'Março'

if mes == '04':
    mes = 'Abril'

elif mes == '05':
    mes = 'Maio'

elif mes == '06':
    mes = 'Junho'

if mes == '07':
    mes = 'Julho'

elif mes == '08':
    mes = 'Agosto'

elif mes == '09':
    mes = 'Setembro'

if mes == '10':
    mes = 'Outubro'

elif mes == '11':
    mes = 'Novembro'

elif mes == '12':
    mes = 'Dezembro'

print('Voce nasceu em', data[0:2], 'de', mes,'de', data[6:10])