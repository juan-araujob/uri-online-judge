V = int(input())
n = 1
while V != 0:
    I = V//50
    V = V-(50*I)
    J = V//10
    V = V-(10*J)
    K = V//5
    V = V-(5*K)
    L = V//1
    print('Teste {}'.format(n))
    print('{} {} {} {}'.format(I, J, K, L))
    print()
    V = int(input())
    n+=1