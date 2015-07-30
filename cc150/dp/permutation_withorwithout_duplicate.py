# permutation
# the nums may contains duplicates

import collections as co

#no duplicate in array
def rec(check,res,path,nums):
	if len(path) == len(nums):
		res.append(path)
		return

	for i in nums:
		if i not in check:
			#path.append(i)
			check.add(i)
			rec(check,res,path+[i],nums)
			check.remove(i)
			#path.pop()

def permutation(nums):
	check = set()
	res = []
	path = []
	rec(check,res,path,nums)
	for i in res:
		print i
	#nums.sort()


# if there is a uniqe path
def dfs(res,path,check,size):
    if len(path) == size:
        res.append(path)
        return
    z = []
    # very important procedure
    # for key,value in check.iteritems():
    #     if value > 0:
    #         z.append(key)
    #print z
    for i in check:
    	if check[i] != 0:
	        check[i] -= 1
	        dfs(res,path+[i],check,size)
	        check[i] += 1
                
def permuteUnique(nums):
    # write your code here
    check = dict(co.Counter(nums))
    #print check
    res = []
    dfs(res,[],check,len(nums))
    return res

nums = [1,1,3,4]
print nums
res = permuteUnique(nums)
for i in res:
	print i

