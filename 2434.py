d, s = map(int, input().split())
menor = s
for i in range(d):
    x = int(input())
    s += x
    if s < menor:
        menor = s
print(menor)