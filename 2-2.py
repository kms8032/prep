# 평균 점수와 학점 등급 계산 프로그램

# 학생들의 세 과목 점수를 입력 받아 평균 점수 계산
# 평균에 따라 학점 등급 부여

# 세과목 점수 입력

# 평균 점수 계산. 점수에따라 등급 결정

math_score = float(input("수학점수를 입력하세요.:"))
science_score = float(input("과학점수를 입력하세요.:"))
english_score = float(input("영어점수를 입력하세요.:"))


def calculate_average(math_score,science_score,english_score) :
    
    return (math_score + science_score + english_score) / 3


if calculate_average(math_score,science_score,english_score) >= 90 :
    print(f"평균점수는 {calculate_average(math_score,science_score,english_score)}, 학점은 A입니다.")
    
elif 90 > calculate_average(math_score,science_score,english_score) >= 80 :
    print(f"평균점수는 {calculate_average(math_score,science_score,english_score)}, 학점은 B입니다.")

elif 80 > calculate_average(math_score,science_score,english_score) >= 70 :
    print(f"평균점수는 {calculate_average(math_score,science_score,english_score)}, 학점은 C입니다.")
    
elif 70 > calculate_average(math_score,science_score,english_score) >= 60 :
    print(f"평균점수는 {calculate_average(math_score,science_score,english_score)}, 학점은 D입니다.")
    
else :
    print(f"평균점수는 {calculate_average(math_score,science_score,english_score)}, 학점은 F입니다.")
    
