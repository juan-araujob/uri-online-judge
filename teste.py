listaa = [0, 0, 0, 0, 0]
a = max(listaa)
print(a)
print(listaa.index(a)+1)
print(len(listaa)-listaa[::-1].index(a))

