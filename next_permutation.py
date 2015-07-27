#coding=utf-8
#注意这里面的逻辑思维：
#从后往前，先找到第一个不是递增的数，index = a
#找到a之后，再去从后往前找到第一个比num[a]大的数
#交换a，b
#对a后面的数进行排序
import pdb
import collections as co
def nextPermutation(num):
    # write your code here
    size = len(num)
    i = size-1
    while i>0 and num[i] <= num[i-1]:
        i-=1
    if i == 0:
        return sorted(num)
    a = i-1
    print num[a]
    b = size-1
    while b>a and nums[b]<=nums[a]:
        b -= 1
    print num[b]
    num[a],num[b] =num[b],num[a]
    num[a+1:] = sorted(num[a+1:])
    
    return num


nums = [2,1,1]
print nums
res = nextPermutation(nums)



#print len(res)
#print nums
print res

#[1,2,3,4,5,6,7,8,9,10,11,11,11,23,4,5,6,7,100,99,98,97,96,95,94,93,92,91,5]
#[1,2,3,4,5,6,7,8,9,10,11,11,11,23,4,5,6,91,5,7,92,93,94,95,96,97,98,99,100]

