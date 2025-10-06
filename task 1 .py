#Task 1: Calculate factorial using a function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ask user for input
num = int(input("Enter a number: "))

# Call the function and display the result
print(f"The factorial of {num} is {factorial(num)}")

