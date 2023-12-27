import sys # sys.stdin.readlin() 사용을 위함

T = int(input()) # 입력과 동시에 문자열을 정수형으로 형변환
		# (입력이 1번 이므로 input()을 사용)
for i in range(T):  # 0~T-1까지 
    a, b = map(int, sys.stdin.readline().split()) 
    print(a+b) #sys.stdin.readlin()은 input()보다          
    #입력 방식이 빠르니 여러 줄을 입력받을 상황에서 반드시 사용한다.
    # map(함수,iterable) : 입력받은 자료형의 각 요소를
    # 함수를 수행한 결과를 묶어서 돌려주는 함수.