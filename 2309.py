n = int(input())
valor = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
awin = bwin = 0
for i in range(n):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    ra = rb = 0
    a = [a1, a2, a3]
    b = [b1, b2, b3]
    for l in range(3):
        posA = valor.index(a[l])
        posB = valor.index(b[l])
        if posA >= posB:
            ra += 1
        elif posB > posA:
            rb += 1
    if ra>rb:
        awin+=1
    else:
        bwin+=1
print(awin, bwin)
