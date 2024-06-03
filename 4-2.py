# 비밀번호 검증기

# 사용자로부터 입력받기
password = input("비밀번호를 입력하세요.:")

# 기준에 충족한지
# 길이가 8자 이상

if len(password) >= 8 :
    # 적어도 하나의 숫가 포함 되어있는지
    for char in password :
        if char.isdigit():
            # 대문자가 있는지
            for char in password:
                if char.isupper():
                    print("안전한 패스워드입니다.")
                    
                else:
                    print("패스워드가 안전하지 않습니다.")
                    break
                    
                    
        else :
            print("패스워드가 안전하지 않습니다,")
            break
else : 
    print("패스워드가 안전하지 않습니다.")