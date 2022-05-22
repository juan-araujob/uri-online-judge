n = int(input())
x = input().split()
word = ''
for i in range(n):
    if x[i][0]+x[i][1]  == 'OB' and len(x[i])<4:
        word += 'OBI'
    elif x[i][0]+x[i][1]  == 'UR' and len(x[i])<4:
        word += 'URI'
    else:
        word += x[i]
    if i<n-1:
        word += ' '
print(word)