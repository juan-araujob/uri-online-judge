n = int(input())+1
matriz = []
for j in range(n):
    linha = []
    a = input().split()
    for k in range(n):
        linha.append(int(a[k]))
    matriz.append(linha)
for l in range(0,n-1):
    for c in range(0,n-1):
         cont = 0
         if matriz[l][c] == 1:
             cont += 1
         if matriz[l][c+1] == 1:
             cont += 1
         if matriz[l+1][c] == 1:
             cont += 1
         if matriz[l+1][c+1] == 1:
             cont += 1
         if cont > 1:
             print('S', end='')
         else:
             print('U', end='')
    print('')