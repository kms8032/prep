num = input("주민번호를 입력하세요.:")

num_list = []
check = [2,3,4,5,6,7,8,9,2,3,4,5]

for i in num :
    num_list.append(int(i))

result = [] 
for a, b in zip(num_list, check):
    result.append(a*b)
    
result = 11 - (sum(result)%11)
if result == num_list[12] :
    print("유효한 주민번호입니다.")
else :
    print("유효하지 않은 주민번호입니다.")