import random

# 대 소 숫자 정의 -> 함수로 정의
def create_password(length): # 길이제한이 있는 무작위한 랜덤한 패스워드를 생성하기 떄문에 매개변수를 길이로 지정
    # 대문자
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 소문자
    small = big.lower()
    # 숫자
    digits = "123456789"
    
    # 랜덤한 대소문자,숫자 뽑기위해 한곳에 찾아보기위해 다 합친다.
    all_characters = big + small + digits
    

# 비밀번호 초기화
    password = ""
# 길이 제한된 random한 password 생성
    for _ in range(length):
        password += random.choice(all_characters)

    return password
# 출력

print(create_password(8))