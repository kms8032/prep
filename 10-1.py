# 당신은 학교 도서관을 위한 간단한 프로그램 작성
# 이 프로그램은 사용자가 도서 제목을 입력하면, 해당 제목을 도서 목록에 추가하는 기능을 해야합니다.
# 사용자가 '종료'라고 입력할 때까지 이 프로세스를 반복하고, 마지막에 전체 도서 목록을 출력합니다.

# 빈 리스트 생성
books = []

# 사용자 입력을 처리하는 루프를 시작
while True :
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력):")
    if title == '종료' :
        break
    books.append(title)

print("도서 목록:",books)