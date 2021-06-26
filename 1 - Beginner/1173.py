# URI Online Judge 1173

valor = int(input())

N = []
N.append(valor)

for i in range(1,10):
    N.append( N[i-1]*2 )

for i in range(10):
    print('N[{:}] = {:}'.format(i, N[i]))