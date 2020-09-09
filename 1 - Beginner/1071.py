## URI Online Judge 1070

X = int(input())
Y = int(input())

if Y < X:
    X, Y = Y, X

summ=0

for i in range(X+1,Y):
    if i%2 != 0:
        summ += i

print(summ)