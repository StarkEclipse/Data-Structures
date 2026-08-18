# def countdown(n):
#     if n == 0:
#         print("blastoff")
#         return
#     print(n)    
#     countdown(n - 1)
# countdown(5)

# def countup(n):
#     if n == 0:
#         return
#     countup(n - 1)
#     print(n)
# countup(5)
# 
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))

# def launch(n):
#     if n == 0:
#         print("go")
#         return
#     print("T-minus", n)
#     launch(n - 1)
# launch(5)

def launch(n):
    if n == 0:
        print("Blast off!")
        return
    print(n)
    launch(n - 1)
launch(15)