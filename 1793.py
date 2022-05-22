n = int(input())
while n != 0:
    x = input().split()
    temp = 10
    for i in range(len(x)):
        try:
            if int(x[i]) + 10 > int(x[i + 1]):
                temp += int(x[i + 1]) - int(x[i])
            elif int(x[i]) + 10 <= int(x[i + 1]):
                temp += 10
        except:
            break
    print(temp)
    n = int(input())