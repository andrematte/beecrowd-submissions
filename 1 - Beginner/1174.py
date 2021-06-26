# URI Online Judge 1174

A = []
tamanho = 100

for i in range(tamanho):
    A.append(float(input()))
    
for i in range(tamanho):
    if A[i] <= 10:
        print('A[{:}] = {:.1f}'.format(i, A[i]))
