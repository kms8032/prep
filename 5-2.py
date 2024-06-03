# 별 패턴 그리기 - 상승과 하강

num = int(input("N 입력:"))

for num in range(1,num+1):
    print(num * "*")
    
for num in range(num-1,0,-1):
    print(num * "*")
    