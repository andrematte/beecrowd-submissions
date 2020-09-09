# Uri Online Judge 1079

N = int(input())


for i in range(0,N):
    Numbers = input()

    num1 = float(Numbers.split()[0])
    num2 = float(Numbers.split()[1])
    num3 = float(Numbers.split()[2])

    print(((2*num1+3*num2+5*num3)/10).__round__(1))