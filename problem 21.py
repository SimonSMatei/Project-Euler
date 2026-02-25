def divisors(num):
    n = 2
    list = []
    while n <= num:
        if num % n == 0:
            list.append(num // n)
        n += 1
    return list

def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

if __name__ == "__main__":
    a = 1
    total_sum = 0
    pairs = []

    while a < 10000:
        if a not in pairs:
            b = sum(divisors(a))
            if a != b:
                if sum(divisors(b)) == a:
                    total_sum += a
                    pairs.append(a)
                    total_sum += b
                    pairs.append(b)
        a += 1

    print(total_sum)