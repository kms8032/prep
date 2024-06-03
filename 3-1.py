# 사전 예약 시스템

# information
# age
# Event_Code
# reservation_date


# E1 : 만 18세 이상
# E2 : All age, date는 짝수만
# E3 : 만 16세 이상, 7의 배수만

# 예약성공 : 예약이 완료 되었습니다.
# 나이 미달 : 나이제한으로 인해 예약이 불가합니다.
# 날짜 제한 : 선택하신 날짜에는 예약이 불가합니다.
# 잘못된 입력 : 잘못된 입력입니다. 프로그램을 종료합니다.

# 정보 입력
age = int(input("나이를 입력하세요.:"))
event_code = input("이벤트 코드를 입력하세요.:")
reservation = int(input("예약하실 날짜를 입력하세요.(1일~30일):"))

# 이벤트 코드에 따른 예약 시스템으로 구축
if age > 0 and 1 < reservation <= 30 :
    
    if event_code == "E1" :
        if age >= 18 :
            print("에약이 완료되었습니다.")
        else :
            print("나이제한으로 인해 예약이 불가합니다.")
            
    elif event_code == 'E2':
        if reservation% 2 == 0 :
            print("예약이 완료되었습니다.")
        else :
            print("선택하신 날짜에는 예약이 불가합니다.")
            
    elif event_code == 'E3':
        if age >= 16 and reservation%7 == 0 :
            print("예약이 완료되었습니다.")
        elif age <= 16 :
            print("나이제한으로 인해 예약이 불가합니다.")
        else :
            print("선택하신 날짜에는 예약이 불가합니다.")
            

    else :
        print("질못된 입력입니다. 프로그램을 종료합니다.")
        

else : 
    print("잘못된 입력입니다. 프로그램을 종료합니다.")