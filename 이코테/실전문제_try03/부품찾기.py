# n = int(input())
# n_list = set(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))
#
# for value in m_list:
#     if value in n_list:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))


def binary_sort(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return "yes"
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return "no"


for value in m_list:
    print(binary_sort(n_list, value, 0, n - 1), end=' ')