# URI Online Judge 1435

N = -1

def imprime_matriz(matriz):
    for i in range(N):
        string = ''
        
        for j in range(N):
            string += "%4d" %matriz[i][j]
        
        print(string[1:])
    
    print("")

def matriz_quadrada(N):
    
    matriz = [[0 for i in range(N)] for i in range(N)]
    
    valor = 1
    cima, baixo = 0, N-1
    esquerda, direita = 0, N-1
    
    meio = N/2 if N%2==0 else (N+1)/2  
        
    while valor <= meio:
        i = esquerda
        while i <= direita:
            matriz[cima][i] = valor
            matriz[baixo][i] = valor
            i+=1
            
        i = cima + 1
        while i < baixo:
            matriz[i][esquerda] = valor
            matriz[i][direita] = valor
            i+=1
            
        valor += 1
        cima += 1 
        baixo -= 1
        esquerda += 1
        direita -= 1        
    
    imprime_matriz(matriz)


while N != 0:
    N = int(input())
    
    if N > 0:
        matriz_quadrada(N)
    

