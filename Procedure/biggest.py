def biggest(a,b,c):
    if a > b and a > c:
        return a
    elif c > b and c > b:
        return c
    else:
        return b

if __name__== '__main__':
    print(biggest(3,2,6))
