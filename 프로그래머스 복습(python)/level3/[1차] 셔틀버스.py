def change_to_str(time):
    minute = str(time // 60).zfill(2)
    second = str(time % 60).zfill(2)
    return minute + ":" + second


def solution(n, t, m, timetable):
    answer = 0

    crew_time_list = []
    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        crew_time_list.append(time)
    crew_time_list.sort()

    bus_time_list = []
    for i in range(n):
        bus_time_list.append(i * t + 9 * 60)

    # 학생 비교 대상 인덱스
    idx = 0
    for time in bus_time_list:
        # m명이하 태우는지 확인
        cnt = 0
        while cnt < m and idx < len(crew_time_list) and crew_time_list[idx] <= time:
            idx += 1
            cnt += 1
        # 학생이 다 타지 않은 경우
        if cnt < m:
            answer = time
        # 학생이 꽉 찼다면 마지막 학생보다는 빨리 타야함
        else:
            answer = crew_time_list[idx - 1] - 1
    return change_to_str(answer)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40", "09:50",
                           "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01", "00:02", "00:03", "00:04"]))

# 18번만 오답
# from collections import deque, defaultdict
#
#
# def change_to_second(time):
#     time = time.split(":")
#     minute = int(time[0])
#     second = int(time[1])
#     return minute * 60 + second
#
#
# def change_to_str(time):
#     minute = str(time // 60)
#     second = str(time % 60)
#     if int(minute) < 10:
#         minute = "0" + minute
#     if int(second) < 10:
#         second = "0" + second
#     return minute + ":" + second
#
#
# def solution(n, t, m, timetable):
#     # n회, t분 간격, 최대 m명
#     start_time = change_to_second("09:00")
#     time_list = []
#     for time in timetable:
#         time_list.append(change_to_second(time))
#     timetable = deque(sorted(time_list))
#     bus_dict = defaultdict(list)
#     bus_list = []
#     temp_start_time = start_time
#     for _ in range(n):
#         bus_list.append(temp_start_time)
#         temp_start_time += t
#
#     bus_idx = 0
#
#     while timetable and bus_idx != n:
#         bus_time = bus_list[bus_idx]
#         student = 0
#         while timetable and student != m:
#             now = timetable[0]
#             # 다음 버스를 타야하는 경우
#             if bus_time < now:
#                 break
#             else:
#                 bus_dict[bus_time].append(timetable.popleft())
#                 student += 1
#         bus_idx += 1
#     if not bus_dict.keys():
#         return change_to_str(bus_list[-1])
#
#     temp = []
#     for key in bus_dict.keys():
#         temp.append([key, bus_dict[key]])
#     time, bus = temp[-1]
#     last_time = bus[-1]
#     if len(bus) == m:
#         return change_to_str(last_time - 1)
#     else:
#         return change_to_str(time)
