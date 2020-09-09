# URI Online Judge 2159
import math

n = int(input())

P = n / math.log(n)
M = 1.25506 * (P)

print('{:.1f} {:.1f}'.format(P, M))
