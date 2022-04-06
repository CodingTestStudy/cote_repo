def change_to_milliseconds(time):
    time = time.split(":")
    hour = float(time[0]) * 60 * 60
    minute = float(time[1]) * 60
    second = float(time[2])
    return (hour + minute + second) * 1000


def delete_s(time):
    return float(time[:-1]) * 1000


def solution(lines):
    start_time_list = []
    end_time_list = []
    answer = 0
    for line in lines:
        line = line.split(" ")
        end_time, process = change_to_milliseconds(line[1]), delete_s(line[2])
        start_time = end_time - process + 1
        start_time_list.append(start_time)
        end_time_list.append(end_time)

    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            # 임의 시간부터 1초간 처리하는 요청 대기수
            if end_time_list[i] > start_time_list[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer


print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))  # 1
print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))  # 2
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))  # 7
