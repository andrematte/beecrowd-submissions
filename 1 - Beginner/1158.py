# URI Online Judge

N = int(input())

for i in range(N):
    teste = input()
    X, Y = int(teste.split()[0]), int(teste.split()[1])
    
    if X % 2 == 1:
        soma = X
    else:
        soma = 0
        
    for y in range(1, 2*Y):
        if (X + y) % 2 == 1:
            soma += X + y
        
    print(soma)