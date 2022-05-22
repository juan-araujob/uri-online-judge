from math import trunc
n = int(input())
for i in range(n):
    x = input()
    tam = len(x)
    nWord = ''
    fWord = ''
    x = x[-1::-1]
    for l in range(tam):
        if l >= trunc(tam/2):
            if 65 <= ord(x[l]) <= 122:
                nWord += chr(ord(x[l])+2)
            else:
                nWord += chr(ord(x[l])-1)
        else:
            if 65 <= ord(x[l]) <= 122:
                nWord += chr(ord(x[l])+3)
            else:
                nWord += x[l]


    print(nWord)
#print(chr(65), chr(122))
