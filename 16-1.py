import random
# 컴퓨터 난수 생성
# 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성합니다.
def rand_num():
    return random.sample(range(10),3)

# 플레이어 입력
# 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
def player_input():
    while True :
        try :
            user_input = input("0~9 사이의 숫자를 중복되지 않는 정수 3개를 입력하세요. (공백으로 갯수 카운트) :")
            user_num = list(map(int,user_input.split()))
            if len(user_num) == 3 and len(set(user_num)) == 3 and all(0 <= num < 10 for num in user_num):
                return user_num
        except ValueError :
            pass
        print("잘못된 입력값입니다.다시 입력하세요.")
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다고 가정합니다.

def compare_number(player_num, computer_num):
    strike = sum(1 for a, b in zip(computer_num, player_num) if a == b)
    ball = sum(1 for num in player_num if num in computer_num) - strike
    return strike, ball

def main() :
    computer_num = rand_num()
    attemps = 0
    strike_outs = 0
    
    while attemps < 5 and strike_outs < 2:
        player_num = player_input()
        attemps += 1
        
        strike, ball = compare_number(computer_num, player_num)
        
        if strike == 3: 
            print("축하합니다! 숫자를 정확히 맞추셨습니다.")
            break
        if strike > 0 or ball > 0:
            print(f"{strike} 스트라이크 , {ball} 볼")
            
        elif strike == 0 and ball == 0:
            strike_outs += 1
            print("스트라이크 아웃")
        print(f"현재까지 시도 횟수 : {attemps}")
        print(f"스트라이크 아웃 횟수 : {strike_outs}")
    else :   
        print("게임오버")
        print(f"컴퓨터의 숫자는 {computer_num}입니다.") 

if __name__ == "__main__":
    main()       
# 게임 패배 조건
# 시도 횟수가 5번 이상일 경우.
# 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우.
#. 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우.

