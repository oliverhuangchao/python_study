def sqrt(x):
    i = 0
    j = x/2+1
    while i<=j:
        mid = (i+j)/2
        sq = mid**2
        if x == sq:
            return mid
        else:
            if sq > x:
                j = mid-1
            else:
                i = mid+1

    return i-1

for i in range(20):
    print "%d sqrt is %d" % (i, sqrt(i))  