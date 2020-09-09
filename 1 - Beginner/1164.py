# URI Online Judge 1164

N = int(input())

for i in range(N):

    sum = 0
    entrada = int(input())

    for j in range(1,entrada):
        if entrada%j==0:
            sum += j

    if entrada == sum:
        print("{} eh perfeito".format(entrada))
    else:
        print("{} nao eh perfeito".format(entrada))