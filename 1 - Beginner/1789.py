# URI Online Judge 1789

while True:
    try:
        N = int(input())
        entrada = [int(i) for i in input().split()]
        
        if max(entrada) < 10:
            print(1)
        elif max(entrada) >= 10 and max(entrada) < 20:
            print(2)
        elif max(entrada) >= 20:
            print(3)
        
    except EOFError:
        break