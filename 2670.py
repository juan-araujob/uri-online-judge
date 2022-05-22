a1 = int(input())
a2 = int(input())
a3 = int(input())
ma1 = a2*2+a3*4
ma2 = a1*2+a3*2
ma3 = a1*4+a2*2
if ma1 <= ma2 and ma1 <= ma3:
    print(ma1)
elif ma2 <= ma1 and ma2 <= ma3:
    print(ma2)
else:
    print(ma3)
