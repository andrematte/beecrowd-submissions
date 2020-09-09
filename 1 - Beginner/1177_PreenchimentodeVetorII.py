# URI Online Judge 1177

T = int(input())
index = 0
N = []

for n in range(int(1000/T)+1):
    for t in range(T):

        N.append(t)
        print("N[{}] = {}".format(index,t))
        index = index + 1
        if index==1000:
            break
