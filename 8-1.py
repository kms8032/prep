temp = float(input("현재 온도(섭씨)를 입력하세요."))

print(f'현재 온도는 {temp}도')

if 30 <= temp :
    print("추천활동 : 스키")
elif 20 <= temp < 30 :
    print("추천활동 : 등산")
elif 10 <= temp < 20 :
    print("추천활동 : 자전거 타기")
else :
    print("추천활동 : 스키")