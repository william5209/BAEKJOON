N = int(input())
a = list(map(int, input().split()))     # 띄어쓰기 간격으로 list 형식으로 저장
v = int(input())

print(a.count(v))                       # list a중 v의 겟수 출력