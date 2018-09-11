# from 1 up to the input number.
def factorial(n):
    i = n
    f = 1
    while i > 0:
        f *= i
        i = i - 1
    return f



if __name__== '__main__':
    print(factorial(4))
