# -*- coding:utf-8 -*-
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    wait_list = deque()
    wait_count = deque()

    while truck_weights or wait_list:
        # 다리를 다 건넌 트럭 처리
        if wait_count and wait_count[0] >= bridge_length:
            wait_count.popleft()
            wait_list.popleft()

        if truck_weights and len(wait_list) < bridge_length and sum(wait_list) + truck_weights[0] <= weight:
            wait_list.append(truck_weights.popleft())
            wait_count.append(0)

        for i in range(len(wait_count)):
            wait_count[i] += 1
        time += 1
    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
