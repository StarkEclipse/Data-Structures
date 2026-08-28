
# low = 0
# high = 6
# mid = (high + low) // 2
# low = mid + 1
# low = 4
# high = 6
# mid = 5

# def binarys(numbers, target):
#     low = 0
#     high = len(numbers) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# numbers = [10, 20, 30, 40, 50, 60, 70]
# result = binarys(numbers, 60)
# print(result)

secret_numbers = [3, 7, 12, 18, 25, 31, 40, 48, 56, 65, 73, 81, 90]

number = int(input("Enter a number you want to find: "))

low = 0
high = len(secret_numbers) - 1
attempts = 0
found = False

while low <= high:
    middle = (low + high) // 2
    middle_number = secret_numbers[middle]
    attempts += 1

    print("Checking:", middle_number)

    if middle_number == number:
        print("Number found!")
        found = True
        break
    elif number < middle_number:
        high = middle - 1
    else:
        low = middle + 1

if not found:
    print("Number not found!")

print("Attempts needed:", attempts)






    

