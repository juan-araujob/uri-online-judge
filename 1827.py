while True:
    try:
        a = int(input())
        quad = a//3
        centro = a//2
        for l in range(a):
            for c in range(a):
                if l >= quad and c >= quad and l < a-quad and c < a-quad:
                    if l == centro and l==c:
                        print('4', end='')
                    else:
                        print('1', end='')
                elif c+l == a-1:
                    print('3', end='')
                elif l == c:
                        print('2', end='')
                else:
                    print('0', end='')
            print()
    except:
        break
        print()