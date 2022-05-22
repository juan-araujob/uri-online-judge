from math import ceil
while True:
    try:
        np, nl, ncl = map(int, input().split())
        n = input().split()
        i = nlinhas = 0
        while np>0:
            espaco = ncl
            while espaco > 0:
                if espaco - len(n[i])<0:
                    espaco = 0
                    break
                else:
                    espaco -= len(n[i]) + 1
                    np -= 1
                    if np == 0:
                        break
                i += 1
            nlinhas += 1
        x = nlinhas/nl
        print(ceil(x))
    except:
        break