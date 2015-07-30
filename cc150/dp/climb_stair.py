import sys
def climbStairs(n):
    # write your code here
    if n < 2:
        return n
    first = 1
    second = 1
    third = 0
    for i in range(2,n+1):
        third = first+second
        first = second
        second = third
    return third

print climbStairs(int(sys.argv[1]))