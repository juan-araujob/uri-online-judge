X = 1
Y = 0
while X != Y:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X>Y:
        print('Decrescente')
    elif Y>X:
        print('Crescente')
    else:
        X=Y=0