import sys
data = list(map(int, sys.stdin.readline().strip()))
dp = [1] * (len(data))
Continue = True


def check(x): # 경우의 수를 추가할 수 있는지 확인
    if x[0] == '0': return False # 해당 문자열이 0으로 시작하면, 경우의 수를 추가할 수 없다. ex) 01 -> 이전의 경우의 수와 동일
    if 1 <= int(x) <= 26: return True # 해당 문자열이 알파벳 범위에 포함된다면 경우의 수 증가
    else: return False # 알파벳 범위에 포함되지 않는다면 경우의 수 증가 X


def wrong_password(x): # 올바르지 않은 암호 코드인지 확인
    if x[0] == 0: return True # 0으로 시작하면 옳지 않은 암호 코드
    for i in range(1, len(x)):
        # 해당 문자가 0으로 끝나면서 알파벳 범위를 벗어난다면 옳지 않은 암호 코드
        if x[i] == 0 and not(1 <= x[i - 1] <= 2): return True


if wrong_password(data): print(0) # 옳지 않은 코드이면 0 출력
else:
    if len(data) == 1: print(1) # 문자의 길이가 1이라면, 1 출력
    else:
        for i in range(1, len(data)):
            # 해당 문자가 0으로 끝나지 않고, 해당 문자열이 알파벳 범위에 포함된다면 ex) 12, 34, ..
            if data[i] != 0 and check(str(data[i - 1]) + str(data[i])):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                # 해당 문자가 0으로 끝나지만, 알파벳 범위에 포함된다면 ex) 10, 20
                if data[i] == 0 and check(str(data[i - 1]) + str(data[i])):
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1]

        print(dp[-1] % 1000000)