# URI Online Judge 1096

I = 0
J = 1
J_init = 1

for i in range(11):
    for j in range(3):

        if (I==0.0 or I==1.0 or I>1.9) and (J==1.0 or (J>=1.8 and J<=2.2) or (J>=2.8 and J<=3.2) or J==4 or J>=4.9):
            print("I={} J={}".format(int(round(I)), int(round(J))))
        elif I==0.0 or I==1.0 or I>1.9:
            print("I={} J={:.1f}".format(int(round(I)), J))
        else:
            print("I={0:.1f} J={1:.1f}".format(I, J))

        J = J + 1.0

    I += 0.2
    J = J_init + 0.2
    J_init = J
