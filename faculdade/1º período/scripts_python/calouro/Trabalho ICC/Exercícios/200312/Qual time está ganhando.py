def pontos(v, e):

    pts_vitoria = v * 3
    pts_empate = e * 1

    pts = pts_vitoria + pts_empate
    return pts


def posicao():

    pts1 = pontos(v1, e1)
    pts2 = pontos(v2, e2)

    if pts1 != pts2:

        if pts1 > pts2:
            print('1')
        else:
            print('2')

    else:

        if sg1 > sg2:
            print('1')
        elif sg1 < sg2:
            print('2')
        else:
            print('1')


v1 = int(input('digite o numero de vitorias do primeiro time: '))
e1 = int(input('digite o numero de empates do primeiro time: '))
sg1 = int(input('digite o saldo de gols do primeiro time: '))

v2 = int(input('digite o numero de vitorias do segundo time: '))
e2 = int(input('digite o numero de empates do segundo time: '))
sg2 = int(input('digite o saldo de gols do segundo time: '))

posicao()