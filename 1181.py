n = int(input())
x = input()
S = 0
matriz = []
for l in range(12):
    linha = []
    for c in range(12):
        a = int(input())
        linha.append(a)
        if l == n:
            S += a
    matriz.append(linha)
if x == 'S':
    print('{:.1f}'.format(S))
elif x == 'M':
    print('{:.1f}'.format(S/12))