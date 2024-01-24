big1 = []
big2 = []
for i in range(0,9,1):
    a = int(input())
    big1.append(a)
    big2.append(a)


big1.sort()
print(big1[8])
number = big2.index(big1[8])
print(number+1)