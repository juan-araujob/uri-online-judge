def fat(n):
    a = n
    while n>1:
        a += a*n-1
        n-=1
    return a
while True:
    a, b = map(int, input().split())
    try:
        a = fat(a)
        b = fat(b)
        print(a+b)
    except:
        break