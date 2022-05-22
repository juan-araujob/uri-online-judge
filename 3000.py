while True:
    try:
        a = int(input())
        for l in range(a):
            for c in range(a):
                if c+l == a-1:
                    print('2', end='')
                elif l == c:
                    print('1', end='')
                else:
                    print('3', end='')
            print('')
    except:
        break