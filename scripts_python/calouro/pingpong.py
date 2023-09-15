from math import sqrt, pow


def emparceiramento():
    print('Digite a posição na chave dos participantes:')

    pos1 = int(input())
    pos2 = int(input())

    diferenca = pos1 - pos2
    diferenca = pow(diferenca, 2)
    diferenca = sqrt(diferenca)

    if pos1 < 0 or pos2 < 0:
        print('Valores inválidos')

    elif pos1 > 16 or pos2 > 16:
        print('Valores inválidos')

    elif pos1 <= 8 and pos2 > 8 or pos1 > 8 and pos2 <= 8:
        print('Final')
    else:
        if pos1 > 8:
            pos1 -= 8
            pos2 -= 8
        if pos1 <= 4 and pos2 > 4 or pos1 > 4 and pos2 <= 4:
            print('SemiFinal')
        else:
            if pos1 > 4:
                pos1 -= 4
                pos2 -= 4
            if pos1 <= 2 and pos2 > 2 or pos1 > 2 and pos2 <= 2:
                print('Quartas')
            else:
                print('Oitavas')


emparceiramento()
