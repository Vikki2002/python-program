def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calling the function with a sample number
number = 5
print(f"Factorial of {number} is : {factorial(number)}")
