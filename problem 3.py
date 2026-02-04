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
    
def factors(num):
    fac = []

    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            fac.append(i)
            fac.append(num / i)
    
    return fac
    

if __name__ == "__main__":
    factor = factors(600851475143)
    
    print(max([i for i in factor if isPrime(i)]))