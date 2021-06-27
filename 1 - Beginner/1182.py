# URI Online Judge 1182

def monta_matriz(rows=12, cols=12):
    matriz = []    
    for i in range(rows):
        line = []
        
        for j in range(cols):
            line.append(float(input()))
        matriz.append(line)
        
    return matriz

L = int(input())  # Linha da Matriz
T = input()       # "S": soma ou "M": media

matriz = monta_matriz()
matriz = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

soma = sum(matriz[L][:])

if T == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(matriz[L][:])))