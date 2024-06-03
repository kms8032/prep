# 세 수의 비교
# 사용자로 부터 세개의 정수를 입력
# 1. 모든 수가 같으면, " 모든수는 같습니다."
# 두수가 같으면, 두수가 같습니다와 같은 두 수도 출력
# 모든 수가 다르면 모든수가 다릅니다. 가장 큰 수는 x입니다. x는 가장 큰 수

num1 = int(input("첫번째 수를 입력하세요."))
num2 = int(input("두번째 수를 입력하세요."))
num3 = int(input("세번째 수를 입력하세요."))

if num1 == num2 == num3 :
    print("모든수가 같습니다.")
elif num1 == num2 or num1 == num2 or num2 == num3 :
    if num1 == num2 :
        print(f"두수가 같습니다. ({num1}와 {num2})")
    elif num1 == num3 :
        print(f"두수가 같습니다. ({num1}와 {num2})")
    elif num2 == num3 :
        print(f"두수가 같습니다. ({num1}와 {num2})")
else :
    if num1 > num2 and num1 > num3 :
        print(f"모든 수가 다릅니다. 가장큰 수는 {num1}")
    elif num2 > num1 and num2 > num3 :
        print(f"모든 수가 다릅니다. 가장큰 수는 {num2}")
    elif num3 > num1 and num3 > num1 :
        print(f"모든 수가 다릅니다. 가장큰 수는 {num3}")