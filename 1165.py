n = int(input())
for i in range(n):
    a = int(input())
    s = 0
    k = 1
    while k <= a or s < 2:
        if a%k == 0:
            s += 1
        k += 1
    if s == 2:
        print('{} eh primo'.format(a))
    else:
        print('{} nao eh primo'.format(a))
