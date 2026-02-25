from math import sqrt

def isPrime(num):
    factors = 0
    
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors += 1
        if factors > 2:
            return False
    
    if factors == 1:
        return True
    else:
        return False
    
def factors(num):
    return [(i, num / i) for i in range(1, int(sqrt(num)) + 1) if num % i == 0]
    

if __name__ == "__main__":
    factor = factors(600851475143)
    
    print(max([i for f in factor for i in f if isPrime(i)]))
