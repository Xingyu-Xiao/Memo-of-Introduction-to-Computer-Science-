def solution(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    length = 2
    last = nums[1]
    if nums[1] - nums[0] > 0:
        p = True
    elif nums[1] - nums[0] < 0:
        p = False
    else:
        return solution(nums[1:])
    for x in nums[2:]:
        if p:
            if x - last < 0:
                length += 1
                p = False
        else:
            if x - last > 0:
                length += 1
                p = True
        last = x
    return length
