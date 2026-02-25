from math import sqrt

def factors(num):
    factorsList = {1}
    for i in range(2, int(sqrt(num))+ 1):
        if num % i == 0:
            factorsList.add(i)
            factorsList.add(num // i)
    return factorsList

def abundantNums():
    abundantList = []
    for n in range(12, 28123):
        sum = 0
        for factor in factors(n):
            sum += factor
        if sum > n:
            abundantList.append(n)
        
    return abundantList

def sumOfAbundantNumbers():
    abundantNumbers = abundantNums()
    sumOfAbundant = set()

    for a in abundantNumbers:
        for b in abundantNumbers:
            num = a + b
            if num > 28123:
                break
            else:
                sumOfAbundant.add(num)
    
    return sumOfAbundant
        
if __name__ == "__main__":
    total_sum = 0
    sum_abundantNums = sumOfAbundantNumbers()

    for num in range(1, 28123):
        if num not in sum_abundantNums:
            total_sum += num

    print(total_sum)
