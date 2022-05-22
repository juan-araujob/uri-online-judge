dentro = fora = 0
n = int(input())
for i in range(n):
    x = int(input())
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
print('{} in\n{} out'.format(dentro, fora))