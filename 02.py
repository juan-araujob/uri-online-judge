N = int(input())
totC = totR = totS = 0
for i in range(N):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    Tipo = str(Tipo)
    if Tipo == 'C':
        totC = totC + Quantia
    elif Tipo == 'R':
        totR = totR + Quantia
    elif Tipo == 'S':
        totS = totS + Quantia
totCOBAIAS = totC+totR+totS
print('Total: {} cobaias'.format(totCOBAIAS))
print('Total de coelhos: {}'.format(totC))
print('Total de ratos: {}'.format(totR))
print('Total de sapos: {}'.format(totS))
print('Percentual de coelhos: {:.2f} %'.format(totC*100/totCOBAIAS))
print('Percentual de ratos: {:.2f} %'.format(totR*100/totCOBAIAS))
print('Percentual de sapos: {:.2f} %'.format(totS*100/totCOBAIAS))