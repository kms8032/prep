# 가상 주식 거래 시뮬레이션


자본금 = int(input("초기 자본금을 입력 하세요. :"))
주식가격 = int(input("주식가격을 입력하세요.:"))
구매주식수 = int(input('구매할 주식 수를 입력하세요.:'))
판매주식가격 = int(input("판매할 때의 주식가격을 입력하세요.:"))


def 계산기(자본금, 주식가격, 구매주식수, 판매주식가격):
    구매후남은자본금 = 자본금 - (주식가격 * 구매주식수)
    예상이익 = ( 판매주식가격 * 구매주식수) -(주식가격 * 구매주식수)
    
    print("구매 후 남은 자본금:",구매후남은자본금)
    if 예상이익 > 0 :
        print("예상이익은:",예상이익)
        print("예상되는 이익입니다.")
    else : 
        print("예상이익은: ",예상이익)
        print("예상되는 손실입니다.")
        


계산기(자본금,주식가격,구매주식수,판매주식가격)