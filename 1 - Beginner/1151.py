# URI Online Judge 1151

N = int(input())
n1 = 0
n2 = 1
string = '0 1'

while (N < 0) and (N > 46):
    N = int(input())
    
for i in range(N-2):
    new = n1 + n2
    
    string += (' ') + str(new)
    
    n1 = n2
    n2 = new
    
    
print(string)
