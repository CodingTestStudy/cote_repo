# "A#" 하나의 문자로 처리하는 함수
def make_list(m):
    m_list = []
    for alpha in m:
        if alpha == "#":
            a = m_list.pop()
            m_list.append(a + alpha)
        else:
            m_list.append(alpha)
    return m_list


# 시간 문자열을 second로 계산하는 함수
def calculate_second(start, end):
    start_total = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    end_total = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
    return end_total - start_total


def solution(m, musicinfos):
    m_list = make_list(m)

    answer = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, melody = musicinfo.split(",")
        time = calculate_second(start, end)
        melody_list = make_list(melody)
        new_melody_list = []
        # 음악 재생 시간보다 멜로디의 길이가 더 긴경우, 해당 재생 시간만큼만 비교 대상
        if time < len(melody_list):
            new_melody_list = melody_list[:time]
        else:
            q, r = divmod(time, len(melody_list))
            new_melody_list.extend(melody_list * q)
            new_melody_list.extend(melody_list[:r])
        repeat, match_cnt = True, 0
        start = 0
        while repeat:
            match_cnt = 0
            for i in range(len(m_list)):
                # index 넘어가는 경우, while문 종료
                if i + start >= len(new_melody_list):
                    repeat = False
                    break
                # 문자열 불일치한 경우, for문 종료
                if m_list[i] != new_melody_list[start + i]:
                    break
                # 일치 count 증가
                else:
                    match_cnt += 1
            start += 1
            # 모든 문자가 서로 일치하는 경우, 리스트에 (시간, 순서, 제목) 순으로 삽입
            if match_cnt == len(m_list):
                answer.append((time, idx, title))
                break
    # 일치하는 멜로디가 없는 경우
    if len(answer) == 0:
        return "(None)"
    answer = sorted(answer, key=lambda x: x[1])
    answer = sorted(answer, key=lambda x: x[0], reverse=True)
    return answer[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# # replace로 # 관련 문자 처리하는 방
# def shap_to_lower(s):
#     s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
#     return s

