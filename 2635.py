a = int(input())
x = []
for i in range(a):
    nome = input()
    x.append(nome)
b = int(input())
for l in range(b):
    maior = quant = 0
    pesq = input()
    for k in range(a):
        if x[k].find(pesq) == 0:
            tam = len(x[k])
            quant += 1
            if tam > maior:
                maior = tam
    if quant > 0:
        print('{} {}'.format(quant, maior))
    else:
        print(-1)