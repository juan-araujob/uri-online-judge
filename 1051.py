s = float(input())
if 0 <= s <= 2000:
    print('Isento')
elif s > 2000:
    if 2000 < s <= 3000:
        i = (s-2000)*0.08
    elif 3000 < s <= 4500:
        i = (s-3000)*0.18+80
    elif s > 4500:
        i = (s-4500)*0.28+350
    print('R$ {:.2f}'.format(i))