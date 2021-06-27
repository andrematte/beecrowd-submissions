# URI Online Judge 1175

tam = 20
N = []

for i in range(tam):
    N.append( int(input()) )
    
    
for i, j in zip(range(tam-1, -1, -1), range(tam)):
    print('N[{:}] = {:}'.format(j, N[i]))
    