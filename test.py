# house robber

def houseRobber(a):
    # write your code here
    if not a:
        return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return max(a)
    #if len(a) == 3:
    #    return max(a[1],a[2]+a[0])
    first = a[0]
    second = a[1]
    for i in range(2,len(a)):
        z = max(second,first + a[i]) 
        first = second
        second = z
    return max(first,second)

a = [9,8,4,5]
#a = [3,8,4]
print houseRobber(a )