n = input().split()
lin = int(n[0])
col = int(n[1])
matriz = []
posAnt = -1
ultimo = -1
resp = 'S'
for j in range(lin):
    linha = input().split()
    matriz.append(linha)
for l in range(lin):
    for c in range(col):
        if matriz[l][c] == '0':
            ultimo = c
        else:
            break
    if ultimo >= posAnt and ultimo == col-1:
        posAnt = ultimo
    elif ultimo >= posAnt:
        posAnt = ultimo+1
    else:
        resp = 'N'
        break
print(resp)