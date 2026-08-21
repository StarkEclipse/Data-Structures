
# low = 0
# high = 6
# mid = (high + low) // 2
# low = mid + 1
# low = 4
# high = 6
# mid = 5

def binarys(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers = [10, 20, 30, 40, 50, 60, 70]
result = binarys(numbers, 60)
print(result)





    

