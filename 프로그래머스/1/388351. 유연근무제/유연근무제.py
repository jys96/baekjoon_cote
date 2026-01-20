def solution(schedules, timelogs, startday):
    answer = 0
    
    def add_10_min(time):
        hour = time // 100
        minute = time % 100
        minute += 10
        if minute >= 60:
            hour += 1
            minute -= 60
        return hour * 100 + minute

    for i in range(len(schedules)):
        target = add_10_min(schedules[i])
        success = True

        for j in range(7):
            weekday = (startday - 1 + j) % 7 + 1

            # 토·일은 검사 제외
            if weekday == 6 or weekday == 7:
                continue

            if timelogs[i][j] > target:
                success = False
                break

        if success:
            answer += 1

    return answer
