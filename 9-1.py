# 출발시간
start_hour = int(input("출발 시(시간)을 입력하세요.:"))
start_min = int(input("출발 시(분)을 입력하세요.:"))

# 도착시간
end_hour = int(input('도착 시(시간)을 입력하세요.:'))
end_min = int(input("도착 시(분)을 입력하세요.:"))

# 이동거리
distance = int(input("이동거리(km)를 입력하세요.:"))

def calculator():
    avg_speed = distance / ((end_hour + (end_min/60))-(start_hour+(start_min/60)))
    print(f'이동거리: {distance}km')
    print(f'출발시간: {start_hour}시 {start_min}분')
    print(f'도착시간: {end_hour}시 {end_min}분')
    print(f"평균속도 : {round(avg_speed,2)}km/h")
    if avg_speed < 60:
        print("속도상태 : 느림")
    elif 60<= avg_speed < 90 :
        print("속도상태 : 보통")
    else :
        print("속도상태 : 빠름")
    return 

calculator()