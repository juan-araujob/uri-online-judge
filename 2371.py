l, c = map(int, input().split())
matriz = []
soma = 0
for i in range(l):
    a = input()
    matriz.append(a)
n = int(input())
for k in range(n):
    lr, cr = map(int, input().split())
    if matriz[lr-1][cr-1] == '#':
        soma += 1
#for u in range(l):
 #  for o in range(c):
  #      if matriz[u][o] == '#' and matrizR[u][o] == 'E':
   #         soma += 1
print(soma)

#for j in range(l):
 #  for o in range(c):
  #    print(matrizR[j][o], end='')
   # print()