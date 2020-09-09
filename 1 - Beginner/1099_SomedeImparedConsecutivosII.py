# URI Online Judge 1099

N = int(input())

for n in range(N):
    sum = 0
    Entrada = input()
    X = int(Entrada.split()[0])
    Y = int(Entrada.split()[1])

    if Y < X:
        X, Y = Y, X

    for i in range(X+1, Y):
        if i%2!=0:
            sum += i

    print(sum)


