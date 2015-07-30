# quick sort for a array

import pdb

def partition_with_dupicate(nums):
	if len(nums) < 2:
		return
	size = len(nums)
	pivot = nums[0]
	start = 0
	end = len(nums)-1
	while start<end:
		while start < end and nums[end] >= pivot:
			end -= 1
		nums[start] = nums[end]
		while start < end and nums[start] < pivot:
			start += 1
		nums[end] = nums[start]
	nums[start] = pivot
	print nums
	start = 0
	while start<size and nums[start] != start:
		start += 1
	end = start
	while end < size and nums[end] == start:
		end += 1
	p = size-1
	if end < size:
		tmp = nums[end]
		while end < p:
			while end<p and nums[p] != pivot:
				p -= 1
			nums[end] = nums[p]
			while end<p and nums[end] == pivot:
				end += 1
			nums[p] = nums[end]

		nums[end] = tmp
	return (start-1,end-1)

# if number do not contains duplicate
def partition_with_no_dupicate(nums):
	if len(nums) < 2:
		return
	size = len(nums)
	pivot = nums[0]
	start = 0
	end = len(nums)-1
	while start<end:
		while start < end and nums[end] >= pivot:
			end -= 1
		nums[start] = nums[end]
		while start < end and nums[start] < pivot:
			start += 1
		nums[end] = nums[start]
	nums[start] = pivot
	return start

def quickSort(nums):
	if len(nums) < 2:
		return nums
	if len(nums) == 2:
		if nums[0] > nums [1]:
			nums.reverse()
			return nums
	#pdb.set_trace()
	mid = partition_with_no_dupicate(nums)
	nums[:mid] = quickSort(nums[:mid])
	#print nums
	nums[mid+1:] = quickSort(nums[mid+1:])
	#print nums
	return nums


# deep copy or shallow copy
def test(nums):
	#nums = [0 for i in range(len(nums))]
	#nums.reverse()
	nums[0] = 1000
#	return nums

#nums = [3,6,7,3,3,3,2,1,5,4,3]
nums = [3,1,2,4,5]
print range(len(nums))
print nums
test(nums)
print nums