from collections import deque
def solution(priorities, location):
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    priorities.sort()
    time = 0
    while q:

        if q[0][0] != priorities[-1]:
            q.append(q.popleft())
        else:
            time += 1
            priorities.pop()
            p, i = q.popleft()
            if i == location:
                return time

print(solution([2, 1, 3, 2], 2))

# d = deque([(v, i) for i, v in enumerate(priorities)])
