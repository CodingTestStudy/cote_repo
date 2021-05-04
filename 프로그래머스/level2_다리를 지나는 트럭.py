from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    time = 0
    bridge = deque()
    wait_count = deque()
    while truck_weights or bridge:
        if wait_count and wait_count[0] == bridge_length:
            bridge.popleft()
            wait_count.popleft()

        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            wait_count.append(0)

        for i in range(len(wait_count)):
            wait_count[i] += 1
        time += 1
    return time

bridge_length = 100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))