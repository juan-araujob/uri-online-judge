n = int(input())
ant = 'sol'
tCasa = 0
tTrab = 0
quantCASA = 0
quantTRAB = 0
for i in range(n):
    a, b = map(str, input().split())
    if ant == 'sol' and a == 'chuva' and b == 'sol':
        if quantCASA == 0:
            tCasa += 1
            quantCASA+=1
        quantTRAB += 1
        quantCASA -= 1
    elif ant == 'sol' and a == 'sol' and b == 'chuva':
        if quantTRAB == 0:
            tTrab += 1
            quantTRAB += 1
        quantCASA += 1
        quantTRAB -= 1
    elif ant == 'sol' and a == 'chuva' and b == 'chuva':
        if quantCASA == 0:
            tCasa += 1
            quantCASA += 1
    elif ant == 'chuva' and a == 'chuva' and b == 'sol':
        quantCASA -= 1
        quantTRAB += 1
    elif ant == 'chuva' and a == 'sol' and b == 'chuva':
        if quantTRAB == 0:
            tTrab += 1
            quantTRAB+=1
        quantCASA += 1
        quantTRAB -= 1
    ant = b
print(tCasa, tTrab)