import random

# 난수를 생성하여 리스트에서 요소를 선택하는 방법

choices = ["가위","바위","보"]
computer_choice = random.choice(choices)

my_choice = input("가위,바위,보 중 하나를 선택하세요.:")
print("컴퓨터의 선택 :",computer_choice)

if my_choice == '가위' and computer_choice == "바위" :
    print("결과 : 당신이 졌습니다.")
elif my_choice == '바위' and computer_choice == "보" :
    print("결과 : 당신이 졌습니다.")
elif my_choice == '보' and computer_choice == "가위" :
    print("결과 : 당신이 졌습니다.")
elif my_choice == '바위' and computer_choice == "가위" :
    print("결과 : 당신이 이겼습니다.")
elif my_choice == '가위' and computer_choice == "보" :
    print("결과 : 당신이 이겼습니다.")
elif my_choice == '보' and computer_choice == "바위" :
    print("결과 : 당신이 이겼습니다.")
else :
    print("결과 : 무승부입니다.")