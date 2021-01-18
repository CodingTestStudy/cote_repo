n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))


def binary_sort(n_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return '1'
        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return '0'


for value in m_list:
    print(binary_sort(n_list, value, 0, n - 1))