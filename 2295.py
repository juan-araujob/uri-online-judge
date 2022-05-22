pa, pg, ra, rg = map(float, input().split())
p1 = ra/pa
p2 = rg/pg
if p1 > p2:
    print('A')
else:
    print('G')