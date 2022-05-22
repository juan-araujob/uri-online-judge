lista = []
while True:
    try:
        x = int(input())
        lista.append(x)
    except:
        break
for i in lista[0:len(lista)]:
    if i == 0:
        print('vai ter copa!')
    else:
        print('vai ter duas!')

