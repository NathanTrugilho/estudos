def maiorde18(d):

    dmaior = d.copy()

    laux = d.keys()
    laux = list(laux)

    for i in range (0, (len(laux))):
        key = laux[i]

        if d[key] < 18:
            dmaior.pop(key)

    return dmaior

print(maiorde18({'sergio': 43, 'almenara': 12, 'alcantara': 56, 'valença': 32, 'mustafa': 15}))