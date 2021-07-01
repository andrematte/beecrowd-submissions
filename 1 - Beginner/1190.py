# URI Online Judge 1190

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
coluna = 10

for i in range(1,11):
    for j in range(11,coluna,-1):
        soma += matriz[i][j]
        contador += 1
    
    if i < 5:
        coluna -= 1
    if i > 5:
        coluna += 1  

                
if T == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/contador))