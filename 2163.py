n = input().split()
lin = int(n[0])
col = int(n[1])
matriz = []
pos = [0,0]
for j in range(lin):
    linha = input().split()
    matriz.append(linha)
lin = lin - 1
col = col - 1
for l in range(1,lin):
    for c in range(1,col):
        if matriz[l][c]== '42' :
            if matriz[l-1][c-1] == '7' and matriz[l-1][c] == '7' and matriz[l-1][c+1] == '7' and matriz[l][c-1] == '7' and matriz[l][c+1] == '7' and matriz[l+1][c-1] == '7' and matriz[l+1][c] == '7' and matriz[l+1][c+1] == '7':
                pos = [l+1,c+1]
print('{} {}'.format(pos[0], pos[1]))