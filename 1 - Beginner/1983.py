# URI Online Judge 1983

N = int(input())
notas = []
matriculas = []

for n in range(N):
    entrada = input().split()
    
    matriculas.append(entrada[0])
    notas.append(float(entrada[1]))
    
max = max(notas)

if max >= 8.0:
    print(matriculas[notas.index(max)])
else:
    print('Minimum note not reached')
    