# 컴퓨터 난수 생성
# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
import random

def com_select():
    return random.sample(range(10),3)
    

# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
def player_selecet():
    player_input = input("0~9 사이의 중복되지 않는 정수를 3개 입력하세요.(공백으로 구분합니다.):")
    player_num = list(map(int,player_input.split()))
    
    return player_num 

# 스트라이크와 볼 갯수 카운트
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
    # 시도횟수 설정
    attempts = 0
    # 스트라이크 아웃 설정
    strike_outs = 0
    # 컴퓨터 선택 저장
    com_num = com_select()
    
    
    # 루프 진행
    while True :
        # 시도 카운트
        attempts += 1
        # 플레이어 숫자 입력
        player_num = player_selecet()
        # 스트라이크 볼 카운트
        strike, ball = count(player_num, com_num)

        # 게임 승리 패배 조건
        
        # 승리
        if strike == 3 :
            print("승리! 게잉에서 이겼습니다.")
            
        # 스트라이크 아웃 카운트
        elif strike == 0 and ball == 0:
            strike_outs += 1
            print("스트라이크 아웃!") 
            
        # 스트라이크 또는 볼이 있을 경우
        elif strike > 0 or ball > 0 :
            print(f"{strike} 스트라이크, {ball} 볼")
            
        print(f'스트라이크 횟수 :{strike_outs}')
        print(f"시도횟수: {attempts}")
        
        if attempts > 4 or strike_outs > 1 :
            print(f"패배! 게임을 종료합니다.\n정답:{com_num}")
            break
        
        
game()