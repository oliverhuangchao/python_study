# adjust a array
# problem in lintcode


def MinAdjustmentCost(self, nums, target):
    # write your code here
    # classical dp problem
    # first find the max value in the array, so each figure should not exceed this range
    # so define a matrix d
    # d[i][j] represents the min different, if nums[i] change to j(j<max_val)
    # it depends on the d[i-1][p], but for p should in (j-target,j+target)
    # then for the last integer, we need to get the result from the last
    
    # 
    int_max = 2**31-1
    max_val = max(nums)
    d = [[0 for i in range(max_val+1)] for j in range(len(nums))]
    for j in range(max_val+1):
        d[0][j] = abs(nums[0]-j)
        
    res = int_max
    for i in range(len(nums)):
        for j in range(max_val+1):
            d[i][j] = int_max
            for k in range(max(0,j-target),min(j+target+1,max_val+1)):
                d[i][j] = min(d[i][j],d[i-1][k])
            d[i][j] += abs(nums[i]-j)
            if i == len(nums)-1:
                res = min(res,d[i][j])
    
    return res