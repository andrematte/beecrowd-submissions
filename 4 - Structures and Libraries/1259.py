# URI Online Judge 1259

N = int(input())
vetor = []
pares = []
impares = []

for n in range(N):
    vetor.append(int(input()))
    
vetor.sort()

for item in vetor:
    if item%2 == 0:
        pares.append(item)
    else:
        impares.append(item)
        
impares.sort(reverse=True)
pares.extend(impares)
vetor = pares

for item in vetor:
    print(item)