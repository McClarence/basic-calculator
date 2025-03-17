# Ask for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# calculating the results based on operation entered
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error!\n        The second number must be a non-zero number"
else:
    result = "Invalid operation!"

# Display the result
print(num1, operation, num2, "=", result)
