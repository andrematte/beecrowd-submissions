# URI Online Judge 1159

X = [int(input())]

while X[-1] != 0:
    X.append( int(input()) )

for x in X[:-1]:
    soma = 0
    for i in range(10):
        if (x+i)%2 == 0:
            soma += x+i
    print(soma)