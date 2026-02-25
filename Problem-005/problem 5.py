from math import sqrt

def factors(num):
    fac = []

    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            fac.append(i)
            fac.append(num / i)
    
    return fac


if __name__ == "__main__":
    list_nums = [i for i in range(1, 21)]
    
    for i in list_nums[::-1]:
        factor = factors(i)
        for n in factor:
            if n in list_nums and n != i:
                list_nums.remove(n)
    
    n = 0
    div = 0

    while div != len(list_nums):
        n += 20
        div = 0

        for num in list_nums:
            if n % num == 0:
                div += 1
            else:  
                break
    
    print(n)
    
