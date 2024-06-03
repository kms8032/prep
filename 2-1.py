# 면적단위 변환기

# 변환 공식
# 1제곱미터 = 10.7639평방피트
# 1에이커 = 4046.86제곱미터

def convert_to_square_feet(square_meters):
    # 제곱미터를 평방피트로 변환하는 코드
    square_feet = 10.7639 * square_meters
    return square_feet

def convert_to_acers(square_meters):
    # 제곱미터를 에이커로 변환하는 코드
    acers = square_meters / 4046.86
    return acers

# 사용자 입력 받기
sqaure_meters = float(input("토지의 면적을 제곱미터 단위로 입력하세요.:"))

if sqaure_meters > 0 :
    print(f'{sqaure_meters}제곱미터는 {convert_to_square_feet(sqaure_meters)} 평방피트입니다.')
    print(f'{sqaure_meters}제곱미터는 {convert_to_acers(sqaure_meters)} 에이커입니다.')
    
else : 
    print("잘못된 입력입니다.")