## URI Online Judge 1072

N = int(input())

inn = 0
outt = 0
for i in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        inn += 1
    else:
        outt += 1

print(inn, "in")
print(outt, "out")
