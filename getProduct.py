# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one
# at i.
# For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120,
# 60, 40, 30, 24]. Ifourinputwas [3, 2, 1],theexpectedoutputwouldbe [2,
# 3, 6].


array = [3, 2, 1]


def products(array):
    newArr = []
    for i in range(0, len(array)):

        mul = 1

        for j in range(0, len(array)):

            if array[i] == array[j]:
                continue
            else:
                mul = mul*array[j]
        newArr.append(mul)
    return newArr


if __name__ == "__main__":
    print(products(array))
