# 투포인터, dict() 사용
def solution(germs):
    answer = [0, len(germs) - 1]
    kind = set(germs)
    germs_dict = dict()
    germs_dict[germs[0]] = 1
    start, end = 0, 0
    while 0 <= start < len(germs) and 0 <= end < len(germs):
        # 종류를 다 찾지 못한 경우, 범위 증가
        if len(germs_dict) < len(kind):
            end += 1
            # 결국 못찾은 경우 반복문 종료, 현재 answer이 정답
            if end == len(germs):
                break
            # germs[end] 개수 증가
            germs_dict[germs[end]] = germs_dict.get(germs[end], 0) + 1
        # 모든 종류를 찾은 경우, 이전 answer과 비교
        else:
            term = end - start + 1
            if term < answer[1] - answer[0] + 1:
                answer = [start, end]
            if germs_dict[germs[start]] == 1:
                del germs_dict[germs[start]]
            else:
                germs_dict[germs[start]] -= 1
            start += 1
    answer[0] += 1
    answer[1] += 1
    return answer



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# # 투포인터(시간초과, 슬라이싱 사용)
# def solution(gems):
#     answer = [0, len(gems) - 1]
#     kind = set(gems)
#     start, end = 0, 0
#     while 0 <= start < len(gems) and 0 <= end < len(gems):
#         if len(set(gems[start:end + 1])) == len(kind):
#             term = end - start + 1
#             if term < answer[1] - answer[0] + 1:
#                 answer = [start, end]
#             start += 1
#         else:
#             end += 1
#     answer[0] += 1
#     answer[1] += 1
#     return answer

# 시간 초과
# def solution(gems):
#     answer = [0, len(gems) - 1]
#     all_cnt = len(set(gems))
#
#     for start in range(len(gems)):
#         term = answer[1] - answer[0]
#         if term + 1 == all_cnt:
#             break
#         gems_set = set()
#         for i in range(start, len(gems)):
#             gems_set.add(gems[i])
#             if len(gems_set) == all_cnt:
#                 now = i - start
#                 if term > now:
#                     answer = [start, i]
#                 break
#
#     answer[0] += 1
#     answer[1] += 1
#     return answer
