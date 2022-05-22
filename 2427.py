quad = 1
L = int(input())
while L >= 2:
    L = L/2
    quad=quad+quad
print(quad**2)
