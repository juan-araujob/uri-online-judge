verif = ['C', 'O', 'B', 'O', 'L']
while True:
    try:
        resp = 'GRACE HOPPER'
        x = input().split('-')
        for i in range(5):
            if x[i][0].upper() != verif[i] and x[i][-1].upper() != verif[i]:
               resp = 'BUG'
               break
        print(resp)
    except:
        break