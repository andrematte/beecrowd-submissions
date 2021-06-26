# URI Online Judge

N = int(input())

for n in range(N):
    numero = int(input())
    divisores = []
    
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores.append(i)
    
    if len(divisores) == 2:
        print('{:} eh primo'.format(numero))
    else:
        print('{:} nao eh primo'.format(numero))