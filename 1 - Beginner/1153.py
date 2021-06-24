# URI Online Judge 1153

N = int(input())
n = N

while (N<=0) and (N>=13):
    N = int(input())
    
for i in range(1, N):
    n = n * (N-i)
    
print(n)