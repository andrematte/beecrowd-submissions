## URI Online Judge 1073

N = int(input())

for i in range(1,N+1):
    if i%2==0:
        print("{}^2 = {}".format(i,i**2))