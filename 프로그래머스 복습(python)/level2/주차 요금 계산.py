from collections import defaultdict, deque
import math


def make_minute(start, end):
    start_time = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    end_time = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
    return end_time - start_time


def calculate_total_fee(time, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    if base_time > time:
        return base_fee
    else:
        return base_fee + math.ceil((time - base_time) / unit_time) * unit_fee


def solution(fees, records):
    answer = []
    car_list = []
    car_minute = defaultdict(int)
    car_dict = defaultdict(list)

    for record in records:
        time, number, in_out = record.split(" ")
        if number not in car_list:
            car_list.append(number)
        car_dict[number].append(time)
    car_list.sort()

    for car in car_list:
        temp = deque(car_dict[car])
        if len(temp) % 2 == 1:
            temp.append('23:59')
        while temp:
            start_time = temp.popleft()
            end_time = temp.popleft()
            car_minute[car] += make_minute(start_time, end_time)
    for minute in car_minute.keys():
        answer.append(calculate_total_fee(car_minute[minute], fees))

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
