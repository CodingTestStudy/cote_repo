def dfs(begin, target, words, visited):
    stack = [begin]
    count = 0
    while stack:
        start = stack.pop()
        if start == target:
            return count

        for i in range(len(words)):
            if visited[i]:
                continue
            end = words[i]
            diff = 0
            for j in range(len(words[0])):
                if start[j] != end[j]:
                    diff += 1
            if diff == 1:
                stack.append(end)
                visited[i] = True
        count += 1
    return count


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    answer = dfs(begin, target, words, visited)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
