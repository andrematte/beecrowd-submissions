# URI Online Judge 1160

# Número de casos para teste
T = int(input())

for t in range(T):
    # Recebe entrada
    entrada = input().split()
    
    # População das cidades A e B
    PA = int(entrada[0])
    PB = int(entrada[1])

    # Taxas de crescimento da população de A e B
    GA = float(entrada[2])
    GB = float(entrada[3])

    tempo_anos = 0
    while (PA <= PB) and (tempo_anos <= 100):
        PA += int(PA * (GA/100))
        PB += int(PB * (GB/100))
        tempo_anos += 1
        
    if tempo_anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('{:} anos.'.format(int(tempo_anos)))