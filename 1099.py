N = int(input())
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y =int(Y)
    tot = 0
    if X >= Y:
        maior = X
        menor = Y
    else:
        menor = X
        maior = Y
    for j in range(menor+1, maior):
        if j%2!=0:
            tot+=j
    print(tot)