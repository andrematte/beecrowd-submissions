# URI Online Judge 1116

N = int(input())

for n in range(N):
    Entrada = input()
    X = int(Entrada.split()[0])
    Y = int(Entrada.split()[1])

    if Y==0:
        print("divisao impossivel")
    else:
        print(X/Y)