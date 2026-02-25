fib = [1, 2]

while fib[-2] + fib[-1] < 4000000:
    fib.append(fib[-2] + fib[-1])

print(sum(i for i in fib if i % 2 == 0))
