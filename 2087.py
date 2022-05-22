n = int(input())
while n > 0:
    lista = []
    posicoes = []
    menores = []
    menor = 101
    quant = 0
    a = 'Bom'
    c = -1
    for i in range(n):
        x = input()
        if len(x) < menor:
            pos = i
            menor = len(x)
        lista.append(x)
    for k in range(n):
        if len(lista[k]) == menor:
            posicoes.append(k)
            menores.append(lista[k])
    c = len(menores)
    while c > 0:
        for l in range(n):
            if menores[c-1] == lista[l][0:menor]:
                quant += 1
                if quant > 1:
                    a = 'Ruim'
                    c = 0
        quant = 0
        c-=1

    print('Conjunto', a)
    n = int(input())