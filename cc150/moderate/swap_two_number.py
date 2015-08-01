# swap two numbers without using any space

def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return (a,b)

print swap(5,6)