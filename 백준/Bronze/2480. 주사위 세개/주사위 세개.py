a, b, c = map(int, input().split())
list = []

if a==b==c:
    print(10000+1000*a)
elif a==b:
    print(1000+100*a)
elif a==c:
    print(1000+100*a)
elif c==b:
    print(1000+100*b)
else:
    list.append(a)
    list.append(b)
    list.append(c)
    list.sort()
    print(100*list[2])