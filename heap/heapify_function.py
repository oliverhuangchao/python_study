import pdb
# heapify solution 1
# nlog(n)
# def heapify(nums):
#     int_max = 2**31-1
#     size = len(nums)
#     odd = True
#     if size % 2 == 0:
#         odd = False
#         nums.append(int_max)
#     size = size/2*2+1
#     for i in range(size):
#         j = i
#         while j > 0:
#             if j%2 == 0 and nums[(j-2)/2] > nums[j]:
#                 tmp = nums[(j-2)/2]
#                 nums[(j-2)/2] = nums[j]
#                 nums[j] = tmp
#                 j = (j-2)/2
#                 continue
#             if j%2 == 1 and nums[(j-1)/2] > nums[j]:
#                 tmp = nums[(j-1)/2]
#                 nums[(j-1)/2] = nums[j]
#                 nums[j] = tmp
#                 j = (j-1)/2
#                 continue
#             break;   


#     if not odd:
#         nums.pop()
#     return nums


# solution two
# use recursive function
def heapify(nums,pos):
    #pdb.set_trace()
    if 2*pos+1 >= len(nums):
        return

    int_max = 2**31-1
    size = len(nums)
    odd = True
    if size % 2 == 0:
        odd = False
        nums.append(int_max)
    size = size/2*2+1
    for i in range(size-1,pos,-2):
        if nums[i] < nums[(i-2)/2] or nums[i-1] <nums[(i-2)/2]:
            tmp = nums[(i-2)/2]
            if nums[i] < nums[i-1]:
                nums[(i-2)/2] = nums[i]
                nums[i] = tmp
                heapify(nums,i)
            else:
                nums[(i-2)/2] = nums[i-1]
                nums[i-1] = tmp
                heapify(nums,i-1)
            
    return
#nums = [3,6,2,4,5,1]
nums = [45,39,32,11,100,2,1]
heapify(nums,0)
print nums




