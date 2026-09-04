# numbers = [5, 3, 8, 4, 2]

# length_n = len(numbers)

# for i in range(length_n):
#     for j in range(length_n - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# print(numbers)

# names = ["Riya", "Aman", "Zoya", "Kabir"]

# n = len(names)

# for i in range(n):
#     for j in range(n - 1):
#         if names[j] < names[j + 1]:
#             names[j], names[j + 1] = names[j + 1], names[j]

# print(names)

numbers = [6, 2, 9, 1, 5]

length = len(numbers)

for i in range(length):
    for j in range(length - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

def sorter(words):
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and len(words[j]) > len(key):
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
    return words


words = ["apple", "kiwi", "banana", "pie", "date"]
sorted_words = sorter(words)
print(sorted_words)
