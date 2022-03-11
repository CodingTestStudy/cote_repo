def solution(s):
    answer = []
    alphabet_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    temp = ""
    for i in range(len(s)):
        if s[i].isdigit():
            answer.append(s[i])
        else:
            temp += s[i]
            if temp in alphabet_dict.keys():
                answer.append(alphabet_dict[temp])
                temp = ""

    return int("".join(answer))


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print((solution("123")))
