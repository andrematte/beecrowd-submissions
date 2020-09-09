# URI Online Judge 1143
a, b, c = 1, 1, 1

N=int(input())

for n in range(0,N):

        b = a**2
        c = a**3
        print("{} {} {}".format(a, b, c))
        b += 1
        c += 1
        a += 1

