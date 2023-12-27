T = int(input())
for i in range(0,T):
    A, B = map(int, input().split(' '))
    i += 1
    print("Case #%d: %d + %d =" %(i,A,B),A+B)