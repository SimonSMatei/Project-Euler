from math import sqrt

def isPrime(num):
    factors = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors += 1
        if factors > 1:
            return False
    if factors == 1:
        return True
    
if __name__ == "__main__":
    list1 = [2, 3]
    n = 1

    while len(list1) < 10001:
        if isPrime(6 * n - 1):
            list1.append(6 * n - 1)
        if isPrime(6 * n + 1):
            list1.append(6 * n + 1)
        
        n += 1
        
    sorted(list1)
    print(list1[10000])