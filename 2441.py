a, b, c = map(int, input().split())
lista = [a, b, c]
nl = sorted(lista)
F1 = int(nl[0])
F2 = int(nl[1])
F3 = int(nl[2])
fimF1 = F1+200
fimF2 = F2+200
fimF3 = F3+200
if F1 == F2 == F3:
    fechada = 20000
elif fimF1 >= F2 and fimF2 >= F3:
    fechada = 60000-(((fimF1-F2)*100)+((fimF2-F3)*100))
elif fimF1 > F2 and fimF2 <= F3:
    fechada = 60000-((fimF1-F2)*100)
elif fimF1 <= F2 and fimF2 > F3:
    fechada = 60000-((fimF2-F3)*100)
print(60000-fechada)
