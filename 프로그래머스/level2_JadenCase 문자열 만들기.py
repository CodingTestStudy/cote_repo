def solution(s):
   s_list = s.split(" ")
   answer = ""
   for value in s_list:
       answer += value.capitalize() + ' '
   return answer[:-1]
    # return ' '.join([w[0].upper() + w[1:].lower() for w in s.split(" ")])



print(solution("3people unFollowed me"))
print(solution("for the last week"))