def solution(video_len, pos, op_start, op_end, commands):
    """video_len : 비디오 길이
        pos : 현재 재생위치
        op_start : 오프닝 시작
        op_end : 오프닝 끝
        commands : 사용자가 선택한 기능"""
    
    def sec(t):
        m,s = map(int,t.split(":"))
        return m * 60 + s
    
    def str(sec):
        m = sec // 60
        s = sec % 60
        if m  < 10:
            m = f'0{m}'
        if s<10:
            s = f'0{s}'
        return f"{m}:{s}"
    
    video = sec(video_len)
    now = sec(pos)
    op_start_sec = sec(op_start)
    op_end_sec = sec(op_end)
    
    for c in commands:
        if op_start_sec <= now <= op_end_sec:
            now = op_end_sec
        
        if c == "next":
            now +=10
        else:
            now -= 10
        if now > video :
            now = video
        if now < 0 :
            now = 0

    if op_start_sec <= now <= op_end_sec:
        now = op_end_sec
    if now >= video:
        return video_len
    return str(now)
        