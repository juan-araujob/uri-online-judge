n = int(input())
for k in range(n):
    x = input()
    tamanhoDiv = int((len(x)-1)/2)
    newWord = ''
    newWord += x[tamanhoDiv::-1]+ x[:tamanhoDiv:-1]
    print(newWord)