print(sum([i for i in range(1, 1000) if i % 5 == 0] + [j for j in range(1, 1000) if j % 3 == 0 and not j % 5 == 0]))
