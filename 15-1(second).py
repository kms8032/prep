# 가위, 바위, 보 게임 확장 버전
# 확장된 가위바보 게임 작성
# 사용자로부터 가위.바위 보, 중 하나를 입력 받고 컴퓨터가 선택한 값과 대결하여 승, 패, 무를 판단하고 결과를 출력
# 게임은 3판 2선승제 로 진행
# 매 개임마다 승, 패 , 무의 결과가 출력
# 게임이 종료되면 전체 승, 무, 패의 결과 최종 승자를 출력
# 사용자가 입력하는 값은 가위, 바위, 보 중 하나여야 하며, 이외의 값이 입력되면 다시 입력

# in, not in 사용 금지




import random

# 컴퓨터 가위바위보 선택
game = ["가위","바위","보"]

# 입력값을 넣고 컴퓨터와 승부
# 게임은 3판 2선승제

win = 0
lose = 0
draw = 0

while True :
    if win == 2 :
        print("최종승자 : 사용자")
        break
    elif lose == 2 :
        print("최종승자 : 컴퓨터")
        break
    player  = input("가위, 바위, 보중 하나를 선택하세요.(단, 이외값 입력시 다시 입력):")
    
    if player == "가위" or player == "바위" or player == '보' :
        com_choice = random.choice(game) # random.choice 사용      # random.choice(매개변수) => 매개변수안에서 랜덤을 선택    # while문안에 있어야 게속 결과값이 바뀌겟지?
        print(f"컴퓨터 선택 : {com_choice}")
    
    if player == "가위" or player == "바위" or player == '보' :
        # 승리
        if player == "가위" and com_choice == "보" :
            win += 1
            print(f"승리 전적 : {win}승 {lose}패 {draw}무")
        elif player == "바위" and com_choice == "가위" :
            win += 1
            print(f"승리 전적 : {win}승 {lose}패 {draw}무")
        elif player == "보" and com_choice == "바위" :
            win += 1
            print(f"승리 전적 : {win}승 {lose}패 {draw}무")
        # 패배
        elif com_choice == "가위" and player == "보" :
            lose += 1
            print(f"패배 전적 : {win}승 {lose}패 {draw}무")
        elif com_choice == "바위" and player == "가위" :
            lose += 1
            print(f"패배 전적 : {win}승 {lose}패 {draw}무")
        elif com_choice == "보" and player == "바위" :
            lose += 1
            print(f"패배 전적 : {win}승 {lose}패 {draw}무")
        # 무승부
        else : 
            draw += 1 
            print(f"무승부 전적 : {win}승 {lose}패 {draw}무")
            