import time

def to_sec(t):
    m, s = map(int, t.split(":"))
    return m * 60 + s

def to_time(sec):
    return f"{sec // 60:02d}:{sec % 60:02d}"

# video_len(동영상 길이), 
# pos(기능 수행 직전 재생 위치), 
# op_start(오프닝 시작 시각), op_end(오프닝 끝나는 시각)
# command(사용자 입력: prev, next)
def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    if op_start <= pos <= op_end:
        pos = op_end

    for job in commands:
        if job == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        else:
            pos -= 10
            if pos < 0:
                pos = 0

        if op_start <= pos <= op_end:
            pos = op_end

    return to_time(pos)
