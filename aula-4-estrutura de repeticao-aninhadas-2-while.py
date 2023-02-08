# 2 while

tabuada = 1

while tabuada <= 10:
    print('TABUADA DO {}:'.format(tabuada))
    i = 1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1