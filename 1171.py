n = int(input())
lista = []
lista2 = []
for i in range(n):
    x = int(input())
    lista.append(x)
    if x not in lista2:
        lista2.append(x)
lista2 = sorted(lista2)
for l in range(len(lista2)):
    num = lista2[l]
    print('{} aparece {} vez(es)'.format(num, lista.count(num)))