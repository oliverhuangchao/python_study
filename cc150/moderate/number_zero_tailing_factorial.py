# find tailing zero in a factorial of n
# factorial of n is defined as !n = n*n-1*n-2*n-3*n-4*...*1

# the idea is trying to find how many five among 0...n

def count_five(n):
    z = []
    i = 1
    while not z or z[-1] != 0:
        z.append(n/(5**i))
        i += 1
    z.pop()
    return sum(z) 


print count_five(105)
