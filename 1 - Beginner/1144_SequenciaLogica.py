# URI Online Judge 1144
a, b, c = 1, 1, 1

N=int(input())
print("{} {} {}".format(a, b, c))

for n in range(0,N*2-1):
    if n%2==0:
        b += 1
        c += 1
        print("{} {} {}".format(a, b, c))
    else:
        a += 1
        b = a**2
        c = a**3
        print("{} {} {}".format(a, b, c))


