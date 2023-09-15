def listaemdicio(l):

    d = {}

    n = int(len(l)/2)

    for i in range (0,n):
        d [l[0+(2*i)]] = l[1+(2*i)]
    return d

print(listaemdicio(l = ['ana', 10, 'pedro', 9, 'maria', 9, 'joao', 10, 'paula', 8]
))