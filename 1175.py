lista = []
k = 19
for i in range(20):
    x = int(input())
    lista.append(x)
for l in range(20):
       print('N[{}] = {}'.format(l, lista[k]))
       k -= 1