def solution(files):
    # (대문자이름, int형 Num, index)
    # 대소문자 구분없이 정렬해야하기 때문에, 동일하게 대문자로 고정
    # 002, 010 과 같은 경우에 대한 정렬을 위해 int형으로 변형
    # 0,1번째 기준으로 정렬한 뒤, index 를 통해 원본 데이터를 사용
    answer = []
    result = []
    for i in range(len(files)):
        head, number, tail = "", "", ""
        next_start = 0
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                next_start = j
                break
            else:
                head += files[i][j]

        for j in range(next_start, len(files[i])):
            if not files[i][j].isdigit():
                next_start = j
                break
            else:
                number += files[i][j]
        cut_idx = -1
        for j in range(len(number)):
            if number[j] == "0":
                cut_idx = j
            else:
                break
        if cut_idx == len(number) - 1:
            number = 0
        else:
            number = number[cut_idx + 1:]

        result.append((head.upper(), int(number), i))

    result.sort()
    for i in range(len(result)):
        answer.append(files[result[i][2]])
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
