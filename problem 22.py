nameList = []
letters = []

with open('name.txt', 'r') as n:
    line = n.readline()
    while line:
        name = line.split(',')
        for i in name:
            nameList.append(i)
        line = n.readline()

nameList.sort()

with open('letters.txt', 'r') as l:
    letter = l.readline()
    while letter:
        letters.append(letter.strip('\n'))
        letter = l.readline()

i = 0
name = ''
letterScore = 0
total = 0

while i < len(nameList):
    name = nameList[i]
    letterScore = 0
    for j in name:
        for l in range(0, len(letters)):
            if j == letters[l]:
                letterScore += (l + 1)
                break
    
    total += ((i + 1) * letterScore)
    
    i += 1

print(total)