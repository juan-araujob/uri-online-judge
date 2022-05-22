X = int(input())
Y = int(input())
s = 0
if X>Y:
    A = Y
    Y = X
    X = A
for i in range(X,Y+1):
    if i % 13 != 0:
        s += i
print(s)