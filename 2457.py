l = input()
x = input().split()
palavra = 0
totPalavras = len(x)
for i in range(totPalavras):
    if x[i].count(l)>0:
        palavra += 1
print('{:.1f}'.format(palavra/totPalavras*100))
