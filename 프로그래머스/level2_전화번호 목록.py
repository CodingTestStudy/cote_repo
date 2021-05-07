def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True
# 핵심 포인트
# 정렬을 했기 때문에, 바로 다음 데이터만 비교해보면 된다.
# 다음 데이터내의 접두어가 되지 않는다면, 그 다다음 데이터들도 마찬가지로 안되기 떄문에
print(solution(["4321", "432"]))
print(solution(["1234", "1235", "567"]))
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))

# 효율적인 코드 (정렬 X)
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         pivot = phone_book[i]
#         for j in range(i+1, len(phone_book)):
#             strlen = min(len(pivot), len(phone_book[j]))
#             if pivot[:strlen] == phone_book[j][:strlen]:
#                 return False
#     return True

# 해쉬 사용(정석)
# def solution(phone_book):
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return True


# 정확성 100, 효율성 50
# from collections import deque
# def solution(phone_book):
#     q = []
#     for value in phone_book:
#         q.append((len(value), value))
#     q.sort()
#     p_list = deque(q)
#
#     while p_list:
#         l, data = p_list.popleft()
#         for l, value in p_list:
#             if data in value[:len(data)]:
#                 return False
#     return True

# import heapq
# def solution(phone_book):
#     q = []
#     for value in phone_book:
#         heapq.heappush(q, (len(value), value))
#
#     while q:
#         l, data = heapq.heappop(q)
#         for l, value in q:
#             if data in value[:len(data)]:
#                 return False
#     return True
