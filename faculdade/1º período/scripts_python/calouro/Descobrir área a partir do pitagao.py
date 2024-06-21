def cat(a, b):
    return (a**2-b**2)**(1/2)

def area(a, b):
    return (cat(a, b)*b)/2

a, b = map(int, input().split())

print(area(a, b))