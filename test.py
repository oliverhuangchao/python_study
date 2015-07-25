def minimumSize( nums, s):
    # write your code here
    if not nums:
        return -1
    z = []
    size = len(nums)
    z.append(nums[0])
    for item in nums[1:]:
        z.append(item+z[-1])
    min_end = 0
    min_start = 0
    a = size-2
    b = size-1
    print z
    res = 100000
    while a >= 0:
        if z[b] == s:
            return b+1
        tmp = z[b]-z[a]
        if tmp == s:
            res = min(res,b-a)
            b-=1
        else:
            if tmp > s:
                b-=1
            else:
                a-=1
    return res

nums = [100,50,99,50,100,50,99,50,100,50]
s = 250
print nums
print minimumSize(nums,s) 