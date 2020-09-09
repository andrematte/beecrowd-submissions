# URI Online Judge 1146

X = int(input())
while X != 0:
    for x in range(1,X+1):
        if x == 1:
            String = "{}".format(x)
        else:
            String += " {}".format(x)

    print(String)
    String = ""
    X = int(input())