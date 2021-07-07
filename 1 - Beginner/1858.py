# URI Online Judge 1858

N = int(input())
entrada = [int(i) for i in input().split()]

resposta = entrada.index(min(entrada)) + 1

print(resposta)