n = int(input())
for i in range(n):
    a = int(input())
    s=0
    for k in range(1, a):
        if a%k == 0:
            s+=k
    if a == s:
        print('{} eh perfeito'.format(a))
    else:
        print('{} nao eh perfeito'.format(a))
