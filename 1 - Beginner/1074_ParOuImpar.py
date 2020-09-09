## URI Online Judge 1074

N = int(input())

for i in range(N):
    X = int(input())
    if X < 0 and X % 2 == 0:
        print("EVEN NEGATIVE")
    elif X > 0 and X % 2 == 0:
        print("EVEN POSITIVE")
    elif X < 0 and X % 2 != 0:
        print("ODD NEGATIVE")
    elif X > 0 and X % 2 != 0:
        print("ODD POSITIVE")
    elif X == 0:
        print("NULL")