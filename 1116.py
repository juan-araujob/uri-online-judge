N = int(input())
for i in range(N):
    x, y = input().split()
    X = int(x)
    Y = int(y)
    if Y == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(X/Y))