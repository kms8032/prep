# 단어 맞추기
import random
# 단어 입력
# 단어를 담을 리스트 생성
com_list = []
# com_list에 3개가 들어있다는걸 나타내주는 count 생성
com_count = 0
# 재 입력을 요구하니 while문 사용 -> 조건문은 com_list에 3개가 찰 때까지
while com_count < 3:
    # 첫, 두, 세 가 들어있는 리스트
    num_list = ["첫", "두", "세"]
    # num_list의 카운트도 만들어주기
    num_list_count = 0
    # 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
    while num_list_count < 3:
        user_word_input = input(f"{num_list[num_list_count]} 번째 단어를 입력하세요\n")
    # 단어의 글자 범위는 5이상 20이하로 제한
        if 5 <= len(user_word_input) <= 20:
            com_list.append(user_word_input)
            num_list_count += 1
            com_count += 1
        else:
            print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
            continue
        

# 유효 범위를 벗어난 단어를 입력할 경우, 재입력을 요구

# 임시 단어

# com_list = ["aabbe", "kkoouu", "qqeerri"]

# 단어 선택
# 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
word_random = com_list[random.randint(0, 2)]
word_random = list(word_random)
print(word_random)
# 게임 시작
# 선택된 단어의 글자 길이
word_random_length = len(word_random)
# 선택된 단어 길이 절반
word_random_half = word_random_length / 2
# 만약 단어 절반의 길이가 절반의 몫보다 크면, 0.5 더하기
if word_random_half > word_random_length // 2:
    word_random_half += 0.5
word_random_half = int(word_random_half)
print(word_random_half)
# 선택된 단어의 index값 리스트
index_list = []
for i in range(word_random_length):
    index_list.append(i)
print(index_list)
# index리스트에서 절반값을 뺀 나머지를 구한다
for i in range(word_random_length - word_random_half):
    del index_list[random.randint(0, word_random_half)]
print(index_list)
# word_random은 정답용, 출력용으로 정답용과 같은 내용의 리스트 생성
word_printed = word_random[:]
# 출력용 리스트에 index값을 넣어 _로 교체
for index in index_list:
    word_printed[index] = "_"
print(word_printed)
# blind 처리된 알파벳은 랜덤하게 선택

# 시도 리스트 생성
count = 1
# 모든 단어를 채울 때 까지 진행되어야 하니 while문 사용
while True:
    # 알파벳 입력
    # 키보드로부터 알파벳 한 글자를 입력받음
    user_input = input(f"{count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n")

    # blind 해제
    # 입력받은 알파벳이 단어 내에 존재할 경우 blind 해제
    if user_input in word_random:
        for index in index_list:
            if user_input == word_random[index]:
                word_printed[index] = user_input
        print(word_printed)
    else:
        print("단어 내 포함되지 않은 알파벳입니다.")
    # 존재하지 않을 경우 "없음" 메시지 출력
    count += 1
    # 게임 종료
    # 단어의 모든 글자를 맞출 경우 게임이 종료
    if word_printed == word_random:
        print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count - 1}")
        break
    
    
