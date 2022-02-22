# Largest 5 digit number in a series

def largestNumber(digits):
    listOne = []

    for i in range(0, len(digits)-4):
        sec = digits[i:i+5]
        listOne.append(int(sec))
    return max(listOne)


print(largestNumber('1234567890'))
