# URI Online Judge 2152

N = int(input())

for n in range(N):
    entrada = [int(i) for i in input().split()]
    
    if entrada[2] == 0: estado = 'fechou'
    else: estado = 'abriu'
    
    print('{:02d}:{:02d} - A porta {}!'.format(entrada[0], entrada[1], estado))