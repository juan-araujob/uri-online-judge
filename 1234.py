while True:
    try:
        x = 'a'
        while x != 'z':
            x = input()
            s = ''
            cont = 1
            for i in range(len(x)):
                if x[i] != ' ':
                    if cont == 1:
                        s += x[i].upper()
                        cont = 2
                    else:
                        s += x[i].lower()
                        cont = 1
                else:
                    s += ' '
            print(s)
    except EOFError:
        break