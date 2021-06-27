# URI Online Judge 1176

N = 62
n1 = 0
n2 = 1
string = '0 1'

for i in range(N-2):
    new = n1 + n2
    
    string += (' ') + str(new)
    
    n1 = n2
    n2 = new
    
    
fib = [int(item) for item in string.split()]

T = -1
while (T<0) or (T>60):
    T = int(input())

for t in range(T):
    entrada = int(input())
    print('Fib({}) = {}'.format(entrada, fib[entrada]))