n = int(input())
cont = 1
while n != 0:
    x = input().split()
    l=0
    tam = len(x)
    while l < tam:
        if l+1 == int(x[l]):
            sort = l+1
            l = tam
        l+=1
    print('Teste {}'.format(cont))
    print(sort)
    print()
    cont += 1
    n = int(input())