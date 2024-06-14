def compare_number(player_num, computer_num):
    strike = sum(1 for a, b in zip(computer_num, player_num) if a == b)
    ball = sum(1 for num in player_num if num in computer_num) - strike
    return strike, ball