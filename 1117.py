v = 0
tot = 0
while v<2:
    n = float(input())
    if 0<= n <= 10:
        tot += n
        v+=1
    else:
        print('nota invalida')
print('media = {:.2f}'.format(tot/2))