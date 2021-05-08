from collections import deque
def solution(n, words):
    words = deque(words)
    answer = []
    repeat = 1
    while True:
        for i in range(1, n + 1):
            # 탈락자 발생 X
            if not words:
                return [0, 0]

            answer.append(words.popleft())
            if len(answer) >= 2 and (answer[-2][-1] != answer[-1][0] or answer.count(answer[-1]) == 2):
                return [i, repeat]
        repeat += 1


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))


# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]