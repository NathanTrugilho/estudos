def mesnum(mes):

    d = {'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
    
    if mes in d:
        return d[mes]
    
    else:
        print('Erro')

print(mesnum())
    



