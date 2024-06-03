value = float(input("기본값을 입력하세요.:"))

def select():
    print("1.더하기")
    print("2.빼기")
    print("3.곱하기")
    print("4.나누기")
    
    select = float(input("선택:"))
    num = float(input("숫자입력:"))
    if select == 1 :
        result = value + num
        print(f"연산결과 : {result}")
    elif select == 2 :
        result = value - num
        print(f"연산결과 : {result}")
    elif select == 3 :
        result = value * num
        print(f"연산결과 : {result}")
    elif select == 4 :
        if num != 0:
            result = value // num
            print(f"연산결과 : {result}")
        else :
            print("에러: 0으로 나눌 수 없습니다.")

select()