n = int(input())
num_list = ['1', '2', '3']
answer = "1"


# 겹치는 부분이 있는지 확인
def check(word):
    for size in range(1, n // 2 + 1):
        if word[-size:] == word[-(size * 2): -size]:
            return False
    return True


# 백트래킹
def dfs(idx, word):
    if idx == n:
        print(int(word))
        exit()

    # 이전 단어하고 겹치지 않는 문자로 넣기
    target = word[-1]
    for j in range(3):
        if num_list[j] != target:
            # 추가된 문자열에 이상이 없을 경우
            if check(word + num_list[j]):
                # 반복 진행
                dfs(idx + 1, word + num_list[j])


dfs(1, answer)
