# 다른 코드 참고 풀이 1
def solution(info, query):
    data = dict()

    # 모든 경우들을 key, value는 리스트 형태로 추후에 삽입
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # 지원자 정보(key)에 해당하는 점수들 삽입
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # 각 data의 점수들 오름차순 정렬
    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()

        # 중간중간 and 있기 때문에
        # 각 조건에 해당하는 점수들
        score_list = data[(q[0], q[2], q[4], q[6])]

        find = int(q[7])
        start = 0
        end = len(score_list)
        mid = 0
        # 이진탐색
        while start < end:
            mid = (start + end)//2
            if score_list[mid] >= find:
                end = mid
            else:
                start = mid+1
        answer.append(len(score_list)-start)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))

# 다른 코드 참고 풀이 2

# from itertools import combinations
#
# def solution(info, query):
#     answer = []
#     info_dict = dict()
#
#     for information in info:
#         temp = information.split(' ')
#         for i in range(5):
#             for comb_info in combinations(temp[:4], i):
#                 sum_info = ''.join(comb_info)
#                 if sum_info in info_dict:
#                     info_dict[sum_info].append(int(temp[-1]))
#                 else:
#                     info_dict[sum_info] = [int(temp[-1])]
#
#     for key in info_dict.keys():
#         info_dict[key].sort()
#     # print(info_dict)
#
#     for commands in query:
#         comb_command = commands.split(' ')
#         target = int(comb_command[-1]) # 점수
#         comb_command = comb_command[:-1] # 점수 외의 요구사항
#
#         while 'and' in comb_command:
#             comb_command.remove('and')
#         while '-' in comb_command:
#             comb_command.remove('-')
#         comb_command = ''.join(comb_command)
#
#         # 이진 탐색
#         if comb_command in info_dict:
#             scores = info_dict[comb_command] # 스펙에 해당하는 점수
#
#             left = 0
#             right = len(scores) - 1
#
#             while left <= right:
#                 mid = (left + right) // 2
#
#                 if target > scores[mid]:
#                     left = mid + 1
#                 elif target <= scores[mid]:
#                     right = mid - 1
#
#             # 이진 탐색을 통해 스펙에 해당하는 점수 중 target 값보다 큰 점수의 개수를 삽입
#             answer.append(len(scores) - left)
#         # 없으면 0명 삽입
#         else:
#             answer.append(0)
#
#     return answer


# 효율성 실패
# def isTrue(applicant, cond):
#     for i in range(len(applicant) - 1):
#         if not (applicant[i] == cond[2 * i] or cond[2 * i] == "-"):
#             return False
#     return True
#
#
# def solution(info, query):
#     answer = []
#     for i in range(len(query)):
#         cond = query[i].split(" ")
#         person = 0
#
#         for j in range(len(info)):
#             applicant = info[j].split(" ")
#             applicant.append(int(applicant.pop()))
#
#             if int(applicant[4]) < int(cond[7]):
#                 break
#             else:
#                 if isTrue(applicant, cond):
#                     person += 1
#
#         answer.append(person)
#     return answer