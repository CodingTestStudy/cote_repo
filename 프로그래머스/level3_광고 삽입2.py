import heapq
def make_num(s):
    num_list = s.split(":")
    hour = int(num_list[0]) * 60 * 60
    minute = int(num_list[1]) * 60
    second = int(num_list[2])
    return hour + minute + second

def make_time(num):
    if num < 0:
        return "00:00:00"
    hour = num // (60 * 60)
    num %= (60 * 60)
    minute = num // 60
    num %= 60
    second = num

    time = ""
    if hour < 10:
        if hour == 0:
            time += "00"
        else:
            time += "0" + str(hour)
    else:
        time += str(hour)
    time += ":"

    if minute < 10:
        if minute == 0:
            time += "00"
        else:
            time += "0" + str(minute)
    else:
        time += str(minute)
    time += ":"

    if second < 10:
        if second == 0:
            time += "00"
        else:
            time += "0" + str(second)
    else:
        time += str(second)
    return time

def solution(play_time, adv_time, logs):
    max_second = make_num(play_time)
    visited = [0] * (max_second + 1)
    adv_second = make_num(adv_time)

    time_list = []
    for value in logs:
        data = value.split("-")
        start = make_num(data[0])
        end = make_num(data[1])
        time_list.append((start, end))
        max_value = -1
        for i in range(start, end + 1):
            visited[i] += 1
            if visited[i] > max_value:
                max_value = visited[i]

    q = []
    for s, e in time_list:
        t1, t2 = 0, 0
        if s + adv_second > max_second:
            t1_length = max_second
        else:
            t1_length = s + adv_second + 1


        for i in range(s, t1_length):
            t1 -= visited[i]
        heapq.heappush(q, (t1, s))

        for i in range(e, e - adv_second - 1, -1):
            t2 -= visited[i]
        heapq.heappush(q, (t2, e - adv_second))

    t, s = heapq.heappop(q)
    print(t, s)
    # print(make_time(s))
    return make_time(s)
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))