n = int(input())
for k in range(n):
    x = input()
    neWord = ''
    if x[0] != ' ':
        neWord += x[0]
    for i in range(1, len(x)):
        if x[i-1] == ' ' and x[i] != ' ':
            neWord += x[i]
    print(neWord)
