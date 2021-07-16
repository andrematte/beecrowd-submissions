# URI Online Judge 1914

N = int(input())

for n in range(N):
    jogada = input().split()
    numeros = input().split()
    
    nome1, nome2 = jogada[0], jogada[2]
    jog1, jog2   = jogada[1], jogada[3]
    num1, num2   = int(numeros[0]), int(numeros[1])
    
    if (num1+num2)%2 == 0: resultado = 'PAR'
    else: resultado = 'IMPAR'
    
    if jog1 == resultado:
        print(nome1)
    else:
        print(nome2)