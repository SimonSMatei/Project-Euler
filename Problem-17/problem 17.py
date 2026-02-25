number = 1
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
total = 0

while number < 1000:
    if number < 20:
        total += len(digits[number - 1])
    elif number < 100:
        stringNum = str(number)
        total += len(tens[int(stringNum[0]) - 2])
        if stringNum[1] != '0':
            total += len(digits[int(stringNum[1]) - 1])
    else:
        stringNum = str(number)
        total += len(digits[int(stringNum[0]) - 1])
        total += 7
        stringNum = stringNum.replace(stringNum[0], '', 1)
        if int(stringNum) != 0:
            total += 3
            if int(stringNum) < 20:
                total += len(digits[int(stringNum) - 1])
            else:
                total += len(tens[int(stringNum[0]) - 2])
                if stringNum[1] != '0':
                    total += len(digits[int(stringNum[1]) - 1])

    number += 1

print(total + 11)
