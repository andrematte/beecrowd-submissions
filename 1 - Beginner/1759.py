# URI Online Judge 1759

N = int(input())
saida = ''

for i in range(N):
    if i < N-1:
        saida += 'Ho '
    else:
        saida += 'Ho!'
        
print(saida)