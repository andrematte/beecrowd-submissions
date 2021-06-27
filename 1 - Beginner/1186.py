# URI Online Judge 1185

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
soma = 0
contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if (i + j + 2) > (len(matriz) + 1):
            soma += matriz[i][j]
            contador += 1
            
if T == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/contador))