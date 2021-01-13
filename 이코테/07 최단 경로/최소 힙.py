# 힙의 default는 최소 힙
# 가장 작은 값 우선순위
# 삽입, 삭제 연산 둘다 O(logN)
# N개 데이터 -> O(NlogN)
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)