N = int(input())
lista = []
temp = 10
for i in range(N):
    x = int(input())
    lista.append(x)
for j in range(len(lista)):
    try:
        if lista[j]+10 > lista[j+1]:
            temp += lista[j+1]-lista[j]
        elif lista[j]+10 <= lista[j+1]:
            temp += 10
    except:
        break
print(temp)