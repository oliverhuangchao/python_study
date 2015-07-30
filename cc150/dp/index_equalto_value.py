# magic index
def rec(nums,start,end):
	mid = (start+end)/2
	if nums[mid] == mid:
		return mid
	else:
		if nums[mid] > mid:
			return rec(nums,start,mid-1)
		else:
			return rec(nums,mid+1,end)

			
# if there is duplicates in the array
def rec2(nums,start,end):
	if start > end or start<0 or end>len(nums):
		return -1
	mid = (start+end)/2
	if nums[mid] == mid:
		return mid
	else:
		# we need to search both side
		left_index = min(mid-1,num[mid])
		left = rec2(nums,start,left_index)
		if left> 0:
			return left
		right_index = max(mid+1,num[mid])
		right = rec2(nums,right_index,end)
		return right

# if the array contains the no duplicate values
def find_index(nums):
	res = rec2(nums,0,len(nums)-1)
	return res


nums = [-5,-2,2,5,10]
print find_index(nums)