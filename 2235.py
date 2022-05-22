a, b, c = map(int, input().split())
if a == b or a == c or b == c:
    print('S')
else:
    if a == b+c or b == a+c or c == a+b:
        print('S')
    else:
        print('N')

