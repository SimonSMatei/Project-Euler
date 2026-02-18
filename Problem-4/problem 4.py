def isPalindrome(num):
    n = str(num)
    if n == n[::-1]:
        return True
    return False

if __name__ == "__main__":
    a = 999
    b = 999

    while not isPalindrome(a*b):
        if b < 900:
            a -= 1
            b = a
        else:
            b -= 1
    
    print(a*b)
