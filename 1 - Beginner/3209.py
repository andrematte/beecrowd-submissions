# URI Online Judge 3209

N = int(input())

for n in range(N):
    entrada = [int(i) for i in input().split()]
    
    K = entrada[0]
    O = entrada[1:]
    
    saida = sum(O) - len(O) + 1
    
    print(saida)