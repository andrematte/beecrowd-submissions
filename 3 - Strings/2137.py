# URI Online Judge 2137

while True:
    try:
        N = int(input())
        arquivo = []

        for n in range(N):
            arquivo.append(input())

        arquivo = sorted(arquivo)
        for n in arquivo:
            print(n)
            
    except EOFError:
        break