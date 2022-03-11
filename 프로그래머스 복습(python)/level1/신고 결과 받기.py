# 본인 코드(밑에 더 간결한 코드 추가)
from collections import defaultdict


def solution(id_list, report, k):
    report_count = dict()
    for user in id_list:
        report_count[user] = 0

    report_dict = defaultdict(set)
    for i in range(len(report)):
        data = report[i].split(" ")
        user, reported_user = data[0], data[1]
        report_dict[user].add(reported_user)

    for user in id_list:
        for target in report_dict[user]:
            report_count[target] += 1

    stopped_id = []
    for user in id_list:
        if report_count[user] >= k:
            stopped_id.append(user)

    result = []
    for user in id_list:
        success = 0
        for stopped in stopped_id:
            if stopped in report_dict[user]:
                success += 1
        result.append(success)
    return result


# more simple code
def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_count = {user: 0 for user in id_list}

    # set() 을 통해 중복 신고 처리, 각 유저들의 신고 당한 횟수 저장
    for data in set(report):
        target = data.split(" ")[1]
        report_count[target] += 1
    # 정지당한 유저 확인 후, 해당 유저의 신고자 값 증가
    for data in set(report):
        user = data.split(" ")[0]
        target = data.split(" ")[1]
        if report_count[target] >= k:
            answer[id_list.index(user)] += 1
    return answer



print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))