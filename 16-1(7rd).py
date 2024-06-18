# 컴퓨터 난수 생성
# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
import random

# 난수 생성 함수
def com_select():
    return random.sample(range(10),3)

# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
def player_select():
    player_input = input("0~9 사이의 중복되지 않는 정수 3개를 입력하세요.(공백으로 구분합니다.): ")
    # 입력값을 리스트로 변환
    player_num = list(map(int, player_input.split())) # player_input을 리스트로 변환시키되 안에 있는 값을 int화 시킨다.
    
    return player_num   # list화 시킨 변수를 출력시킨다.

# 스트라이크, 볼이 몇개인지 출력하는 함수 
def strike_ball_count(player_num, com_num):
    strike = sum( 1 for a,b in zip(player_num, com_num) if a == b)
    ball = sum( 1 for num in player_num if num in com_num) - strike # 중복되지 않게 스트라이크를 뺀다.
    return strike, ball # 출력값이 strike 와 ball을 출력하도록 한다.

# 게임 패배 조건
# 시도 횟수가 5번 이상일 경우.
# 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
#. 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.

# 게임 시작 함수
def game_start():
    # 시도, 스트라이크 아웃 설정
    attempts = 0
    strike_outs = 0
    
    # 랜덤한 정수 생성
    com_num = com_select()
    
    # 루프 설정
    while True :
        attempts += 1
        player_num = player_select()
        
        # 카운트 
        strike, ball = strike_ball_count(player_num, com_num)
        
        # 승리
        if strike == 3 :
            print("승리! 게임을 종료합니다.")
            break
        
        # 스트라이크 볼이 있을 경우
        elif strike > 0 or ball > 0:
            print(f"{strike} 스트라이크, {ball} 볼")
            
        # 없을 경우 -> 스트라이크 아웃
        else :
            strike_outs += 1
            print("스트라이크 아웃!")
            
            
        # 패배
        if attempts == 5 or strike_outs >= 2 :
            print(f"패배!\n정답:{com_num}\n게임을 종료합니다.")
            break
        
        print(f"시도횟수 : {attempts}")
        print(f"스트라이크 아웃 횟수 : {strike_outs}")
        
        
game_start()            
        
        