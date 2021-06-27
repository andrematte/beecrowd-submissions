# URI Online Judge 1178

X = float(input())

N = [X]
print('N[{}] = {:.4f}'.format(0, N[0]))

for i in range(1, 100):
    N.append(N[i-1]/2)
    print('N[{}] = {:.4f}'.format(i, N[i-1]/2))
