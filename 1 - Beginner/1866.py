# URI Online Judge 1688

N = int(input())
for n in range(N):

    S = int(input())
    soma = 0

    for s in range(S):
        if s%2 == 0: soma += 1
        elif s%2 == 1: soma -= 1

    print(soma)
