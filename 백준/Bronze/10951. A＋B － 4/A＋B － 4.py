while(True):
    # try 내부에 있는게 애러가 나면 except내부의 코드로 예외 처리한다.
    try:
        A, B = map(int, input().split(' '))
        print(A+B)
    except:
        break