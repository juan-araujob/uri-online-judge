N = int(input())
for i in range(N):
    L = int(input())
    soma = 0
    for l in range(L):
        x = input()
        for k in range(len(x)):
            soma += ord(x[k])-65+l+k
    print(soma)