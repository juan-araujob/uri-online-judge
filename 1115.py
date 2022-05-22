v = 0
while v == 0:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X == 0 or Y == 0:
        v = 1
    else:
        if X>0 and Y>0:
            print('primeiro')
        elif X<0 and Y>0:
            print('segundo')
        elif X<0 and Y<0:
            print('terceiro')
        elif X>0 and Y<0:
            print('quarto')