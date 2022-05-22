n = int(input())
for i in range(n):
    nword = ''
    x = input()
    e = int(input())
    for l in range(len(x)):
        ordem = ord(x[l])-e
        if ordem >= 65:
            nword += chr(ordem)
        else:
            nword += chr(91-(65-ordem))
    print(nword)
