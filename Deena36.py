def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact


n = int(input("Enter number of people: "))
r = int(input("Enter number of seats: "))

p = factorial(n) // factorial(n - r)

print("Total possible arrangements:", p)
