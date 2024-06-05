# 사용자로부터 여러 문장으로 구성된 하나의 문자열을 입력을 받음
# 이 문자열에서 사용자가 지정된 단어가 몇 번 등장하는지 카운트하는 프로그램 작성
# 단어와 문장은 공백으로 구분
# 결과는 단어의 출현 횟수를 출력

# 프로그램은 두번의 입력을 받음
# 1st 검사할 전체 문자열
# 2nd 출현 빈도를 확인할 단어
# 함수는 input, print 및 형변환 함수 이외의 함수는 사용하지 않습니다.
# in, not in 사용금지


# 알고리즘 힌트
# 문자열의 각 문자를 순회하며 공백이나 구두점을 만나면 그전까지의 문자들을 하나의 단어로 간주
# 각 단어를 추출할때마다 입력받은 특정 단어와 비교하여 카운트
# 모든 문자를 순회한 후, 카운트한 값을 출력

first_str = input("문자열 입력:")

second_str = input("단어 입력:")

count =  0

check_str = first_str.split()
for i in range(0,len(check_str)) :
    
    if check_str[i] == second_str:
        count += 1
    
print(f'단어 {second_str}의 출현 빈도 :',count)

