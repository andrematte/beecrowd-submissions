# URI Online Judge 1142

X = int(input())
count = 1

for x in range(1,X+1):
    String = ''

    for i in range(4):
        if i == 0:
            String += "{}".format(count)
        elif i == 3:
            String += " PUM"
        else:
            String += " {}".format(count)
        count += 1
    print(String)
