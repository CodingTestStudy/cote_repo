from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용

# 리스트를 사용해서 큐 구현 가능하지만, 시간 복잡도에서 손해

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
