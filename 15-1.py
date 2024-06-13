# 가위, 바위, 보 게임 확장 버전
# 확장된 가위바보 게임 작성
# 사용자로부터 가위.바위 보, 중 하나를 입력 받고 컴퓨터가 선택한 값과 대결하여 승, 패, 무를 판단하고 결과를 출력
# 게임은 3판 2선승제 로 진행
# 매 개임마다 승, 패 , 무의 결과가 출력
# 게임이 종료되면 전체 승, 무, 패의 결과 최종 승자를 출력
# 사용자가 입력하는 값은 가위, 바위, 보 중 하나여야 하며, 이외의 값이 입력되면 다시 입력

# in, not in 사용 금지


import random

# 가위 바위 보 중 하나 선택
choices = ['가위', '바위', '보']


# 승점
win = 0
draw = 0
lose = 0
game = True

while game :
    com_choice = random.choice(choices)
    my_choice = input("가위, 바위. 보 중에 하나를 선택하세요.")
    print(f"컴퓨터 : {com_choice}")
    
   
    # 내가 졌을 때
    if my_choice == "가위" and com_choice == "바위" :
        lose += 1
        print(f"패배! 현재 전적 {win}승 {lose}패 {draw}무")
        
    elif my_choice == "바위" and com_choice == "보" :
        lose += 1
        print(f"패배! 현재 전적 {win}승 {lose}패 {draw}무")
        
    elif my_choice == "보" and com_choice == "가위" :
        lose += 1
        print(f"패배! 현재 전적 {win}승 {lose}패 {draw}무")
        
        
    # 내가 이겼을때
    elif my_choice == "바위" and com_choice == "가위" :
        win += 1
        print(f"승리! 현재 전적 {win}승 {lose}패 {draw}무")
        
    elif my_choice == "보" and com_choice == "바위" :
        win += 1
        print(f"승리! 현재 전적 {win}승 {lose}패 {draw}무")
        
    elif my_choice == "가위" and com_choice == "보" :
        win += 1
        print(f"승리! 현재 전적 {win}승 {lose}패 {draw}무")
        
    
        
    # 무승부 일때
    elif my_choice == com_choice :
        draw += 1  
        print(f"무승부! 현재 전적 {win}승 {lose}패 {draw}무")
        
     # 가위 바위 보중 다른것을 냈을때
    else : 
        print("잘못된 입력값입니다.")
    
          

    if win == 2 :
        print(f"현재 전적 {win}승 {lose}패 {draw}무 \n최종승자 : 사용자 ")
        game = False
        
    elif lose == 2 : 
        print(f"현재 전적 {win}승 {lose}패 {draw}무 \n최종승자 : 컴퓨터")
        game = False