lista = []
while True:
    try:
        a, b, c = map(int, input().split())
        lista.append(a)
        lista.append(b)
        lista.append(c)
    except:
        break
for i in range(0, len(lista), 3):
    a = lista[i]
    b = lista[i+1]
    c = lista[i+2]
    if a == b == c:
        print('*')
    elif a == b:
        print('C')
    elif a == c:
        print('B')
    else:
        print('A')
