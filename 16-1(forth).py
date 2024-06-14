
# 컴퓨터 난수 생성
# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
import random


def rand_num():
    return random.sample(range(10),3)
    
# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
def player_input():
    player_input = input("0~9사이의 중복되지 않은 정수를 입력하세요.(공백으로 구분합니다.):")
    player_num = list(map(int,player_input.split()))
    return player_num

# 스트라이크, 볼
def compare_number(player_num, computer_num):
    strike = sum( 1 for a,b in zip(player_num, computer_num) if a== b)
    ball = sum(1 for num in player_num if num in computer_num ) - strike
    
    return strike, ball

def main() :
    computer_num = rand_num()
    attempts = 0
    strike_outs = 0

    while attempts < 5 and strike_outs < 2 :
        player_num = player_input()
        attempts += 1
        
        strike, ball = compare_number(player_num, computer_num)
        
        if strike == 3:
            print("승리! 경기에서 이겼습니다.")
            
        else :
            print(f'{strike} 스트라이크, {ball} 볼')
            
        if strike == 0 and ball == 0 :
            strike_outs += 1
        
        print(f"시도 : {attempts}")
        print(f"스트라이크 아웃 : {strike_outs}")
    else:
        print("게임종료")
        print(f"정답: {computer_num}")
        
main()
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.
# 게임 패배 조건
# 시도 횟수가 5번 이상일 경우.
# 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
#. 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.

