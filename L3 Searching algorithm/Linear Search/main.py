# numbers = [5, 12, 8, 20, 3]
# numbers = [10, 25, 7, 42, 18]

numbers = [4, 9, 2, 7, 15, 6]

target = 15
for number in numbers:
    if target in numbers:
        print(f"{target} is in the list")
        break

contacts = ["Alice", "Bob", "Charlie", "David", "Eve"]
who = input("Who are you looking for?\n")
for contact in contacts:
    if who in contacts:
        print(f"{who} is contact number {contacts.index(who) + 1}.")
        break
    else:
        print("Contact not found")
        break


        
