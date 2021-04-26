from collections import deque

def solution(board, moves):
    q = deque(moves)
    bucket = []
    answer = 0
    while q:
        now = q.popleft() - 1

        for i in range(len(board)):
            if board[i][now] == 0: continue
            else:
                bucket.append(board[i][now])
                board[i][now] = 0
                break

        if len(bucket) >= 2:
            if bucket[-1] == bucket[-2]:
                answer += 2
                bucket.pop()
                bucket.pop()
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))

