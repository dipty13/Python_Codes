def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smaller(a,b):
    if a < b:
        return a
    else:
        return b

def smallest(a,b,c):
    return smaller(a,smaller(b,c))

def median(a,b,c):
    if a == biggest(a,b,c):
        return bigger(b,c)
    elif b == biggest(a,b,c):
        return bigger(a,c)
    else:
        return c
if __name__== '__main__':
    print(median(2, 2, 1))
