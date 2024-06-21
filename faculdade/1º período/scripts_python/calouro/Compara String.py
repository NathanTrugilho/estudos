x = input('informe a primeira string: ')
y = input('informe a segunda string: ')

print('String1:', x)
print('String2:', y)

print('Tamanho de', x, ':', len(x), 'caracteres')
print('Tamanho de', y, ':', len(y), 'caracteres')

if len(x) == len(y):
    print('As duas strings possuem o mesmo tamanho')

else:
    print('As duas strings possuem tamanhos diferentes')

if x == y:
    print('As duas strings possuem o mesmo conteudo')

else:
    print('As duas strings possuem conteudos diferentes')