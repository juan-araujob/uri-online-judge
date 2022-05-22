N = int(input())
m2 = m3 = m4 = m5 = 0
lista = input().split()
for i in range(N):
    if int(lista[i])%2==0:
        m2 += 1
    if int(lista[i])%3==0:
        m3 += 1
    if int(lista[i])%4==0:
        m4 += 1
    if int(lista[i])%5==0:
        m5 += 1
print('{} Multiplo(s) de 2'.format(m2))
print('{} Multiplo(s) de 3'.format(m3))
print('{} Multiplo(s) de 4'.format(m4))
print('{} Multiplo(s) de 5'.format(m5))