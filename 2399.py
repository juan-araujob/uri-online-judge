n = int(input())
ant = fim = 0
bombas = []
for i in range(n):
    x = int(input())
    bombas.append(x)
for k in range(0, n):
    if k == 0:
        try:
            soma = bombas[k]+bombas[k+1]
        except:
            soma = bombas[k]
    elif k == n-1:
        soma = bombas[k-1] + bombas[k]
    else:
        soma = bombas[k-1] + bombas[k] + bombas[k+1]
    print(soma)