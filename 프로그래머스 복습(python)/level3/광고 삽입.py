def change_to_str(time):
    hour = time // 60 // 60
    minute = (time - (hour * 60 * 60)) // 60
    second = (time - (hour * 60 * 60) - (minute * 60))
    return ":".join([str(hour).zfill(2), str(minute).zfill(2), str(second).zfill(2)])


def change_to_second(time):
    time = time.split(":")
    hour = int(time[0]) * 60 * 60
    minute = int(time[1]) * 60
    second = int(time[2])
    return hour + minute + second


# dp 사용 (누적값 시용 -> 여러 구간 탐색할 필요 X, 전체 구간 한번만 탐색하면서 계산)
def solution(play_time, adv_time, logs):
    play_time = change_to_second(play_time)
    adv_time = change_to_second(adv_time)

    dp = [0] * (play_time + 1)
    for log in logs:
        log = log.split("-")
        start = change_to_second(log[0])
        end = change_to_second(log[1])
        dp[start] += 1  # 시청 시작 시간
        dp[end] -= 1  # 시청 종료 시간

    for i in range(1, play_time):
        dp[i] += dp[i - 1]
    for i in range(1, play_time):
        dp[i] += dp[i - 1]

    answer = 0
    max_cnt = -1

    # 광고가 끝나는 시점을 기준으로
    for end_time in range(adv_time - 1, play_time):
        temp = dp[end_time] - dp[end_time - adv_time]  # 광고 시작~끝
        if temp > max_cnt:
            max_cnt = temp
            answer = end_time - adv_time + 1

    return change_to_str(answer)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
