import random

def create_password(length):
    big = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"
    small = big.lower()
    digits ="123456789"
    
    all_character = big + small + digits
    

    # 패스워드 초기화
    password = ""

    # 지정된 길이만큼 랜덤 문자 선택
    for _ in range(length):
        password += random.choice(all_character)
        
    return password


created_password  = create_password(8)
print(created_password)