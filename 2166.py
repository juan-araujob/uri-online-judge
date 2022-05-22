N = int(input())
y = N
X = 2
if N == 0:
    y = 0.5
while y == 0.5 or y != 1:
    if y == 0.5:
        X = 1
        break
    X = 2+1/X
    y = y-1
if y == 1:
    X = 1+1/X
print('{:.10f}'.format(X))