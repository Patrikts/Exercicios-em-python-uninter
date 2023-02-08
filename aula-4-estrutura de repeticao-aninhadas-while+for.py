tabuada = 1

while tabuada <= 10:
    print('TABUADA DO {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada + i))
    tabuada += 1