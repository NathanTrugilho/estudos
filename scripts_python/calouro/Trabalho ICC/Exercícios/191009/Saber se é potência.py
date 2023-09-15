import math

def log(x):

    log = math.log2(x)

    if float.is_integer(log) and x !=1:
        print('True')
    else:
        print('False')

num = int(input('digite o número que será verificado: '))
log(num)

