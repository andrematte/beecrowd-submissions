# URI Online Judge 1156

S = 1

d = 2

for n in range(3,40,2):
    S += n/d
    d = d * 2
    
print('{:.2f}'.format(S))