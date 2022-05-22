while True:
    z = input().split()
    if z == ['0']:
        break
    a, b, c = z
    a, b, c = int(a), int(b), int(c)
    x = ((a*b)/(c/100))**0.5
    print(int(x))