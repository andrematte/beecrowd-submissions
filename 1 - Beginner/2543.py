# URI Online Judge 2543

while True:
    try:
        entrada = input().split()
        N, id = int(entrada[0]), entrada[1]

        contador = 0

        for n in range(N):
            entrada = input().split()
            
            if entrada[0] == id and entrada[1] == '0':
                contador += 1
            
                
        print(contador)
        
    except EOFError:
        break 