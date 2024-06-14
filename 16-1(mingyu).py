# 야구 게임

# 컴퓨터 난수 생성
# 난수 저장할 리스트
import random


com_list = []
# 저장되는 횟수 카운트
count = 0
# 3개의 중복되지 않는 정수가 저장될 때 까지 반복해야 하니 while에 조건문 사용
while count < 3:
    # 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성
    random_num = random.randint(0, 9)
    # 중복값 검사
    for num in range(count):
        if random_num == com_list[num]:
            break

    com_list.append(random_num)
    count += 1
print(com_list)

# 시도 횟수 카운트, 아웃 카운트 생성
game_count = 1
o = 0
# 게임 종료 조건을 만족할때까지 반복해야 하니 while문 사용
while True:
    # 플레이어 입력
    # 플레이어 입력값을 저장할 리스트
    user_list = []
    # 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력합니다.
    for _ in range(3):
        user_input = int(input("0~9 사이의 정수를 입력하세요: "))
        user_list.append(user_input)
    
    # 스트라이크, 볼 카운트
    s = 0
    b = 0
    
    # 스트라이크, 볼 확인
    for i in range(3):
        for j in range(3):
            if user_list[i] == com_list[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
    # game_count와 user_input 출력
    print(f"시도 {game_count}: 입력한 숫자 - {user_list[0]} {user_list[1]} {user_list[2]}")
    
    # 스트라이크, 볼 검증 후 결과 중계
    if s == 0 and b == 0:
        o += 1
        print(f"결과: {s} Strike, {b} Ball, {o} Out")
    else:
        print(f"결과: {s} Strike, {b} Ball")

    game_count += 1

    # 게임 패배 조건
    # 시도 횟수가 5번 이상일 경우.
    if game_count == 5:
        print(f"게임 종료: 패배 (시도 횟수 5회 초과)\n정답: {user_list[0]} {user_list[1]} {user_list[2]}")
        break
    elif o == 2:
        print(f"게임 종료: 패배 (스트라이크 아웃 2회 이상)\n정답: {user_list[0]} {user_list[1]} {user_list[2]}")
        break
    # 스트라이크 아웃 횟수가 2회 이상

    # 게임 승리 조건
    # 플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    if user_list == com_list:
        print(f"게임 종료: 승리\n정답: {com_list[0]} {com_list[1]} {com_list[2]}")
        break