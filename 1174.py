lista = []
for i in range(100):
    x = float(input())
    lista.append(x)
for l in range(100):
    if lista[l]<=10:
        print('A[{}] = {:.1f}'.format(l, lista[l]))