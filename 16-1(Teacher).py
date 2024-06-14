# 중복되지 않은 난수 값 3개 생성(0 ~ 9)

count_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    # 사용자로부터 정수 3개 입력
    

    # strike, ball 판별
    # strike out 판별

    # 게임종료 조건(승리,패배)
    
    # 승리 조건
    #  - strike 3개
    if count_strike >= 3:
        print(f"사용자 승리!")
        break
    
    
    # 패배 조건
    #  - strike out 2번
    #  - 시도 회수 5번 이상
    if count_strike_out >= 2 or count_trial >= 5:
        print(f"사용자 패배")
        break
    
    