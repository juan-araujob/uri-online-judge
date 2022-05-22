n = int(input())
print(0, end=' ')
a = 0
b = 1
for i in range(n-2):
    print(b, end=' ')
    s = a + b
    a = b
    b = s
print(b)
