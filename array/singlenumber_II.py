# only one of the number exist not triple times
def singleNumberII(A):
    # write your code here
    z = [0]*32
    for item in A:
        i = 1
        index = 0
        while index < 32:
            if item & i > 0:
                z[index] += 1
            i = i << 1
            index += 1
    print z
    #z.reverse()
    #print z
    res = 0
    for i in range(32):
        if z[i] % 3 != 0:
            res += (2**i)
        
    return res


A =[1,1,2,3,3,3,2,2,4,1]
print singleNumberII(A)