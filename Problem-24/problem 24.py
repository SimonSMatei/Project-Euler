from itertools import permutations

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
num = ''
permList = []

for i in perm:
    num = ''
    for j in i:
        num += str(j)
    permList.append(num)


print(permList[999999])
