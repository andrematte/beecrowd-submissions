# URI Online Judge 1187

def monta_matriz(rows=12, cols=12):
    matriz = []    
    for i in range(rows):
        line = []
        
        for j in range(cols):
            line.append(float(input()))
        
        matriz.append(line)
        
    return matriz

T = input()       # "S": soma ou "M": media

matriz = monta_matriz()
matriz.reverse()
soma = 0
contador = 0

for i in range(6-1):
    soma += sum(matriz[i][(1+i):(-1-i)])
    contador += len(matriz[i][(1+i):(-1-i)])
    
                
if T == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/contador))