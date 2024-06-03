# 출석 점수 프로그램

# 계산법
# 20점에서 결석시간에 비례하여 점수 차감
# 식 : 20점 - (20 * 결석시간 수 / 총 수업시간)

# 총 수업시간 : 시수/주 * 15

# 지각 처리 규칙 : 지각 3회는 결석 1시간 처리

# 결석 처리 : 총 수업시수의 1/4 초과할 경우 학점 미부여

def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    
    calculate_attendance_score = 20 - (20 * ((absence_hours + (tardy_count // 3))/ (hours_per_week *15)) )
    
    return calculate_attendance_score

hours_per_week = int(input("주당 수업 시간을 입력하세요.:"))
absence_hours = int(input("결석한 수업 시간을 입력하세요.:"))
tardy_count = int(input("지각횟수를 입력하세요."))

score = calculate_attendance_score(hours_per_week,absence_hours,tardy_count)
re_score = f'{score:.2f}'

if  absence_hours + (tardy_count // 3) < (hours_per_week * 15)//4 :
    print(f'당신의 출석 점수는 {re_score}점입니다.')
    
else : 
    print("당신의 출석 점수는 F (학점 미부여)점입니다.")