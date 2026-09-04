numbers = [6, 2, 5, 3, 1]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1 
    numbers[j + 1] = key
print(numbers)
# Best Case: O(n)
# Average ands Worst Case O(n^2)
# Best Case O(1)

