# 이 게임은 컴퓨터가 생성한 중복되지 않는 3개의 난수를 플레이어가 맞추는 게임
# 각 시도마다 입력한 숫자와 컴퓨터의 숫자를 비교하여 스트라이크와 볼의 개수를 알려줌
# 게임은 플레이어가 정답을 맞추거나 패배 조건에 도달할 때 까지 진행

# 게임 규칙
# 1. 컴퓨터 난수 생성
# 게임 시작시 0-9사이의 중복되지 않는 정수 3개 생성

# 2. 플레이어 입력
# 플레이어는 키보드를 통해 0 ~ 9 사이의 정수를 3개 입력
# 예외 처리는 하지 않습니다. 올바른 입력이 들어온다는 가정

# 3. 게임 패배 조건
# 시도 횟수가 5번 이상일 경우
# 스트라이크 아웃 횟수가 2번 이상일경우

# 4. 게임 승리 조건
# 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우

import random

# 3개의 난수 생성하는 함수 생성
def com_random():
    return random.sample(range(10),3)

# 플레이어의 추측과 비밀번호를 비교하여 스트라이크와 볼을 계산하는 함수 생송
def check_guess(secret_num, guess):
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == secret_num[i]:
            strike += 1
        elif guess[i] in secret_num:
            ball += 1
            
    return strike, ball

def play():
    # 게임 시작
    print("게임을 시작합니다. 컴퓨터가 숫자를 생성했습니다.")
    
    # 컴퓨터가 난수 생성
    secret_num = com_random()
    
    # 변수 초기화
    attemps = 0
    strikes_out = 0
    
    # 게임 루프
    while True :
        # 입력받기
        guess = input("0부터 9가지의 숫자 중 중복되지않는 3개의 숫자를 입력하세요.")
        
        # 스트라이크 볼 계산
        strike, ball = check_guess(secret_num,guess)
        
        # 결과 출력
        print(f"스트라이크 : {strike}, 볼 : {ball}")
        
        # 게임 종료 조건 확인
        if strike == 3:
            print("축하합니다! 정답을 맞췄습니다!")
            break
        attemps += 1
        if attemps >= 5:
            print("게임 오버! 시도 횟수를 모두 사용했습니다.")
            break
        if strike == 0:
            strikes_outs += 1
        if strikes_out >= 2:
            print("게임 오버! 스트라이크 아웃 횟수가 2번 이상입니다.")
            break

# 게임 실행
if __name__ == "__main__":
    play ()