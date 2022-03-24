from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        ban = banned_id[i]
        user = users[i]

        # 서로 길이가 다름면 비교 대상 자체가 아님
        if len(user) != len(ban):
            return False

        for j in range(len(user)):
            if ban[j] == "*":
                continue
            if ban[j] != user[j]:
                return False
    return True


def solution(user_id, banned_id):
    # 제재 대상 모든 경우의 수, 각각의 경우에서 banned_id 대상이 되는지 검사하는 방식
    permu = list(permutations(user_id, len(banned_id)))
    banned_list = []

    for users in permu:
        if not check(users, banned_id):
            continue
        else:
            # 제재 대상 가능 유저들
            users = set(users)

            # 중복 제거
            if users not in banned_list:
                banned_list.append(users)

    return len(banned_list)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
