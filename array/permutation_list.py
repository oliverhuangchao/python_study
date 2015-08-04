# 写出所有的permutationlist，并找到第k个
# 关键的部分是 while循环里面的那些
# 一个小的corner部分是最开始的n和k都需要分别-1才可以
# 这个是需要注意的
def fac(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

def getPermutation(n, k):
    a = range(1,n+1)
    n -= 1 
    k -= 1
    tmp = fac(n)
    res = []
    while n > 0:
        x = k/tmp
        k %= tmp
        res.append(str(a[x]))
        del a[x]
        tmp /= n
        n -= 1
    
    res.append(str(a[0]))
    return ''.join(res)


print getPermutation(5,5)
