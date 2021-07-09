def dfs(begin, target, words, visited):
    stack = [begin]
    count = 0
    while stack:
        x = stack.pop()

        # 현재 찾은 단어가 target인 경우
        # 즉각 return 최소 횟수를 찾기 때문
        if x == target:
            return count

        # 단어 목록들 확인
        # x와 단어 1개 차이나는 단어들 모두 stack에 삽입
        # 삽입된 단어들은 다시 x로 다뤄지고, 위 과정 반복하여
        # 변환 최소 횟수 찾기 가능
        for i in range(len(words)):
            # 이전에 다뤘던 단어라면 해당 단어 검사 X
            if visited[i]:
                continue

            now = words[i]
            diff = 0
            for j in range(len(words[0])):
                if x[j] != now[j]:
                    diff += 1
            if diff == 1:
                # 조건에 맞으면 방문 처리 및 stack에 삽입하여 단어로 선정
                visited[i] = True
                stack.append(now)
        count += 1
    return count

def solution(begin, target, words):
    # 단어 목록에 target이 존재하지 않는 경우
    if target not in words:
        return 0
    answer = 0
    words_length = len(words)
    # 단어 목록 내의 각각 단어에 방문여부 확인
    visited = [False for _ in range(words_length)]
    answer = dfs(begin, target, words, visited)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))