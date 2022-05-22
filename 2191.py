N = int(input())
i=1
while N != 0:
    lista = []
    for j in range(N):
        X, Y = map(int, input().split())
        lista.append(X-Y)
    a = max(lista)
    print('Teste {}'.format(i))
    if a > 0:
        m1 = lista.index(a)+1
        m2 = len(lista)-lista[::-1].index(a)
        print('{} {}'.format(m1, m2))
    else:
        print('nenhum')
    print()
    i += 1
    N = int(input())
