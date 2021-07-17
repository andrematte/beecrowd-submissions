# URI Online Judge 3161

entrada = [int(i) for i in input().split()]
N, M = entrada[0], entrada[1]

frutas = [input().lower() for i in range(N)]
codigos = [input().lower() for i in range(M)]
codigo = ''.join(codigos)

gosta = []

for fruta in frutas:
    if fruta in codigo or fruta in codigo[::-1] :
        print("Sheldon come a fruta {}".format(fruta))
    else:
        print("Sheldon detesta a fruta {}".format(fruta))


