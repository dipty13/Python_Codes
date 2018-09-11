def is_friend(a):
    if a[0] == "D" or a[0] == "N":
        return True
    else:
        return False

if __name__== '__main__':
    print(is_friend("Dian"))
