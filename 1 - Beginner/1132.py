# URI Online Judge 1133

X = int(input())
Y = int(input())
soma = 0

if Y < X:
    X, Y = Y, X

for i in range(X,Y+1):
    if i%13!=0:
        soma += i

print(soma)