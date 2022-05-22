nGI = 1
inter = gremio = empate = 0
while nGI == 1:
    i, g = input().split()
    i = int(i)
    g = int(g)
    if i>g:
        inter += 1
    elif g>i:
        gremio += 1
    else:
        empate += 1
    nGI = int(input('Novo grenal (1-sim 2-nao)'))
print('{} grenais'.format(inter+gremio+empate))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))
if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')