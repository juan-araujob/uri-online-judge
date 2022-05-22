n = int(input())
x = list(map(int, input().split()))
menor = x[0]
pos = 0
for i in range(len(x)):
    if x[i] < menor:
        menor = x[i]
        pos = i
print('Menor valor:', menor)
print('Posicao:', pos)