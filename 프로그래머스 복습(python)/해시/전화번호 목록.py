def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))


def solution(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        temp = ""
        for num in number:
            temp += num
            if temp in hash_map and temp != number:
                return False
    return True
