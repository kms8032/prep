# 컴퓨터 난수 생성
# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
import random

def com_select():
    return random.sample(range(10),3)


# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
def player_select():
    player_input = input("0~9 사이의 중복되지 않는 정수를 입력하세요.(공백으로 정수 구분):")
    player_num = list(map(int, player_input.split()))
    return player_num

# 스트라이크, 볼 카운트
def count(player_num, com_num):
    strike = sum( 1 for a,b in zip(player_num, com_num) if a == b)
    ball = sum( 1 for num in player_num if num in com_num) - strike
    return strike, ball

# 게임 패배 조건
# 시도 횟수가 5번 이상일 경우.
# 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
#. 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.
def game():
    # 횟수 설정
    attempts = 0
    # 스트라이크 아웃 설정
    strike_outs = 0
    # 컴퓨터 난수 설정
    com_num = com_select()
    
    # 루프 설정
    while True :
        # 시도 카운트
        attempts += 1
        # 플레이어 넘버 설정
        player_num = player_select()
        # 스트라이크 볼 확인
        strike, ball = count(player_num, com_num)
        
        # 승리
        if strike == 3 :
            print("승리! 게임에서 이겼습니다.\n게임을 종료합니다.")
            break
        
        elif strike > 0 or ball > 0 :
            print(f"{strike} 스트라이크, {ball} 볼")
            
        else :
            strike_outs += 1
            print("스트라이크 아웃!")
            
        print(f"시도 횟수:{attempts}")
        print(f"스트라이크 아웃 횟수 : {strike_outs}")
        
        # 패배 
        if strike_outs == 2:
            print("스트라이크 아웃 두번으로 패배하였습니다. 게임을 종료합니다.")
            break
        elif attempts == 5:
            print("시도횟수 초과여서 패배하였습니다. 게임을 종료합니다.")
            break
        
        
        
game()