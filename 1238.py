N = int(input())
for i in range(N):
    s1, s2 = map(str, input().split())
    if len(s1)>len(s2):
        maior = len(s1)
    else:
        maior = len(s2)
    j=0
    newWord = ''
    while j < maior:
          if j < len(s1) and j < len(s2):
            newWord += s1[j]+s2[j]
          elif j < len(s1):
            newWord += s1[j]
          elif j < len(s2):
            newWord += s2[j]
          j+=1
    print(newWord)