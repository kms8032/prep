import random

def generate_unique_numbers():
    return random.sample(range(10), 3)

def get_player_input():
    while True:
        try:
            user_input = input("0~9 사이의 숫자 3개를 공백으로 구분하여 입력하세요: ")
            user_numbers = list(map(int, user_input.split()))
            if len(user_numbers) == 3 and len(set(user_numbers)) == 3 and all(0 <= num < 10 for num in user_numbers):
                return user_numbers
        except ValueError:
            pass
        print("잘못된 입력입니다. 다시 시도하세요.")

def compare_numbers(computer_numbers, player_numbers):
    strike = sum(1 for a, b in zip(computer_numbers, player_numbers) if a == b)
    ball = sum(1 for num in player_numbers if num in computer_numbers) - strike
    return strike, ball

def main():
    computer_numbers = generate_unique_numbers()
    attempts = 0
    strike_outs = 0
    
    while attempts < 5 and strike_outs < 2:
        player_numbers = get_player_input()
        attempts += 1
        
        strike, ball = compare_numbers(computer_numbers, player_numbers)
        
        if strike == 3:
            print("축하합니다! 숫자를 정확히 맞추셨습니다!")
            break
        
        if strike > 0:
            print(f"{strike} 스트라이크")
        if ball > 0:
            print(f"{ball} 볼")
        
        if strike == 0 and ball == 0:
            strike_outs += 1
            print("스트라이크 아웃!")
        print(f"현재까지 시도 횟수: {attempts}")
        print(f"스트라이크 아웃 횟수: {strike_outs}")

    if attempts >= 5 or strike_outs >= 2:
        print("게임 오버!")
        print(f"컴퓨터의 숫자는 {computer_numbers}였습니다.")

if __name__ == "__main__":
    main()
