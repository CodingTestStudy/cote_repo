# 문자열 압축
def solution(s):
  answer = len(s)
  # 1개의 단위(step)부터 압축 단위를 늘려가며 확인
  for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step]  # 앞에서부터 step만큼 문자열 추출
    count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for i in range(step, len(s), step):
      # 이전 상태와 동일하다면 압축 횟수 증가 
      if prev == s[i:i+step]:
        count += 1
      # 다른 문자열이 나왔다면
      else:
        compressed += str(count) + prev if count >= 2 else prev
        count = 1
        prev = s[i:i+step]
    
    # 남은 문자열 처리
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))
  return answer

s = 'aaaabbabbabb'
print(solution(s))