# add two number just use bit manipulation
import pdb
def aplusb(a,b):
    # if b == 0:
    #     return a
    # x = a ^ b # sum without carry
    # y = (a & b) << 1 # only carry, but move 1 bit right
    # return aplusb(x,y)
    while b!=0:
        carry = a&b
        a = a^b
        b = carry<<1
    return a

# check whether a number is a positive or not
def isPositive(a):
    flag = (a & 0x8000) >> 1
    if flag > 1:
        return False
    else:
        return True
# if it is a negetive, change to -a
def turnPositive(a):
    if not isPositive(a):
        return aplusb((~a),1)
    else:
        return a

# decide which value is bigger
def compare(a,b):
    tmp = 0x4000
    while tmp > 0:
        x = tmp & a
        y = tmp & b
        if x == y:
            tmp = tmp >> 1
        else:
            if x > y:
                return 1
            else: 
                return -1
    return 0



a = 3
b = -2
print "a is %d, b is %d" % (a,b)
print aplusb(a,b)
