def solution(nums):
    nums_set = set(nums)
    cnt = len(nums_set)
    max_num = len(nums) // 2
    if cnt > max_num:
        return max_num
    else:
        return cnt