x = input()
S = 0
cont = 0
matriz = []
for l in range(12):
    linha = []
    for c in range(12):
        a = int(input())
        linha.append(a)
        if c-l > 0:
            S += a
            cont += 1
    matriz.append(linha)
if x == 'S':
    print('{:.1f}'.format(S))
elif x == 'M':
    print('{:.1f}'.format(S/cont))