def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # choice = input("Enter choice (1/2/3/4): ")
    choice = '3'

    if choice in ('1', '2', '3', '4'):
        # num1 = float(input("Enter first number: "))
        num1 = 33
        # num2 = float(input("Enter second number: "))
        num2 = 3

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input!")

    # again = input("Do you want to perform another calculation? (yes/no): ")
    # if again.lower() != 'yes':
    break
