n = int(input())
lista2 = []
for i in range(n):
    a, b, c, d = map(str, input().split())
    lista = [a, b, c, d]
    lista2.append(lista)
while True:
    try:
        resp = 'Tente Novamente!'
        z = input().split()
        for l in range(n):
            if z[0] == lista2[l][0]:
                for k in range(1, 4):
                    if lista2[l][k] == z[1]:
                        resp = 'Uhul! Seu amigo secreto vai adorar o/'
                        break
        print(resp)
    except:
        break
