import random

def get_vaild_word():
    # 단어를 담을 리스트 생성
    words = []
    # 입력한 단어를 리스트에 넣는 반복문 작성
    for i in range(3):
        while True :
            word = input(f"{i+1}번째 5자 이상 20자 이하 단어를 입력하세요.:")
            # 글자수 맞으면 추가 아니면 재입력
            if 5 <= len(word) <= 20 :
                words.append(word)
                break
            else :
                print("5자 이상 20자이하의 단어를 다시 입력하세요.:")
    return words 

def game():
    print("게임을 시작합니다.")
    
    # com_list 에 입력 단어 리스트 저장
    com_list = get_vaild_word()
    # com_list 에서 단어 선택
    word_random = random.choice(com_list)
    # 단어 길이 확인
    word_random_length = len(word_random)
    # 단어 반틈만 가리기위한 변수
    word_random_half = (word_random_length + 1) // 2
    
    index_list = random.sample(range(word_random_length),word_random_half)
    # 선택된 단어의 각 문자를 블라인드 처리하여 표시
    word_printed = ['_' if i in index_list else word_random[i] for i in range(word_random_length) ]
    
    print