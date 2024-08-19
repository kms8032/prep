import random

def get_vaild_word():
    # 단어를 담을 리스트 생성
    words = []
    # 리스트에 담을 단어 작성
    for i in range(3):
        while True:
            word = input(f"{i+1}번쨰 단어를 입력하세요.(5~20자):")
            # 5자 이상 20자 이하의 단어가 맞는지 확인후 맞으면 추가 아니면 재입력
            if 5 <= len(word) <= 20:
                words.append(word)
                break # while 문에 대한 break이기 때문에 break를 하면 for문 i가 증가하고 다시 while문이 시작이 됨
            else:
                print("5자 이상 20자 이하의 단어를 입력하세요.")
    return words

def word_game():
    print("게임을 시작합니다!")
    
    # 입력한 단어를 리스트에 생성하는 함수 호출
    com_list = get_vaild_word()
    # 리스트 중 하나를 선택하여 저장
    word_random = random.choice(com_list)
    # 선택된 단어가 몇글자인지 저장
    word_random_length = len(word_random)
    #
    word_random_half = (word_random_length + 1) // 2
    
    # 무작위 빈칸을 만들기 위한 리스트
    index_list = random.sample(range(word_random_length), word_random_half) # word_random_length안에서 word_random_half개를 골라 index list에 저장 
    # index_list 통해 블라인드 처리
    word_printed = ["_" if i in index_list else word_random[i] for i in range(word_random_length)] # word_random_length의 범위 안에서 i값이 증가하면 앞에 있는 수식이 성립이 되면 "_"가 입력이 됨
    #
    print("Blind 처리된 단어:", ''.join(word_printed))
    # 리스트화 시켜놓은 word_printed를 문자열로 붙인다.
    # ex) ['','','',''] -> ''
    count = 1
    while True :
        user_input = input(f'{count}번째 시도, 알파벳 한 글자를 입력하세요.:')
        
        if user_input in word_random:
            for i,char in enumerate(word_random):
                if char == user_input:
                    word_printed[i] = user_input
            print(''.join(word_printed))
        else :
            print("단어 내 포함되지 않은 알파벳입니다.")
            
        if ''.join(word_printed) == word_random :
            print(f"Clear = 선택된 단어 : {word_random}, 총 시도 횟수 : {count}")
            break
        
        count += 1
        
word_game()  