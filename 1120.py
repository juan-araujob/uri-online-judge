while True:
    nWord = '0'
    a = input().split()
    if a[0] == a[1] == '0':
        break
    for i in range(len(a[1])):
        nErro = a[0]
        nAtual = a[1][i]
        if nAtual != nErro:
            nWord+=nAtual
    print(int(nWord))

