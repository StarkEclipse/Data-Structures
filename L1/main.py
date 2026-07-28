# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(self.name, "says: Woof! Woof!")

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# # Create objects
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)

# # Use object methods
# dog1.show_details()
# dog1.bark()

# print()

# dog2.show_details()
# dog2.bark()

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Grade: ", self.grade)

# student1 = Student("Onore", 16, 11)
# student2 = Student("Aero", 17, 12)

# student1.show_details()
# student2.show_details()

class Car:
    def __init__(self, brand, speed = 0):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"Vroom! Speed is now {self.speed}")

    def brake(self):
        self.speed -= 10
        print("Screech! Speed is now:", self.speed)

car1 = Car("Ferarri", 200)
car2 = Car("Nissan", 160)

car1.accelerate()
car2.brake()