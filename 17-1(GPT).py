import random

def get_valid_word():
    words = []
    for i in range(3):
        while True:
            word = input(f"{i+1} 번째 단어를 입력하세요 (5~20자): ")
            if 5 <= len(word) <= 20:
                words.append(word)
                break
            else:
                print("5자 이상, 20자 이하의 단어를 입력하세요.")
    return words

def main():
    print("게임을 시작합니다!")
    
    com_list = get_valid_word()
    word_random = random.choice(com_list)
    word_random_length = len(word_random)
    word_random_half = (word_random_length + 1) // 2
    
    index_list = random.sample(range(word_random_length), word_random_half)
    print(index_list)
    word_printed = ['_' if i in index_list else word_random[i] for i in range(word_random_length)]
    
    print("Blind 처리된 단어:", ''.join(word_printed))
    
    count = 1
    while True:
        user_input = input(f"{count}번째 시도, 알파벳 한 글자를 입력하세요: ")
        
        if user_input in word_random:
            for i, char in enumerate(word_random):
                if char == user_input:
                    word_printed[i] = user_input
            print(''.join(word_printed))
        else:
            print("단어 내 포함되지 않은 알파벳입니다.")
        
        if ''.join(word_printed) == word_random:
            print(f"Clear - 선택된 단어: {word_random}, 총 시도 횟수: {count}")
            break
        
        count += 1

if __name__ == "__main__":
    main()
