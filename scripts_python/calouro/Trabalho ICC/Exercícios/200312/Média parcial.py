def mediap():
    if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
        return (0.85 * (n1 + n2)) / 2 + 0.15 * n3

    else:
        return -1


n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))

if mediap() >= 7:
    print(2)
elif 7 > mediap() >= 3:
    print(1)
elif 0 <= mediap() < 3:
    print(0)
else:
    print(-1)
