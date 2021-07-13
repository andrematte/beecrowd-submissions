# URI Online Judge 1161

def fatorial(n):
    if n == 0: return 1
    return n * fatorial(n-1)

while True:
    try:
        entrada = [int(i) for i in input().split()]
        n1 = fatorial(entrada[0])
        n2 = fatorial(entrada[1])
        print(n1 + n2)
    
    except EOFError:
        break