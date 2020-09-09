# URI Online Judge 1080

Maior = 0
Posicao = 0

for i in range(100):

    Numero = int(input())

    if Numero > Maior:
        Maior = Numero
        Posicao = i+1

print(Maior)
print(Posicao)