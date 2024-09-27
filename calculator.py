# Define the calculator function
def calculator(num1, num2, operation):
    try:
        if operation == '1':  # Addition
            results = num1 + num2
            return f"Result: {num1} + {num2} = {results}"
        
        elif operation == '2':  # Subtraction
            results = num1 - num2
            return f"Result: {num1} - {num2} = {results}"
        
        elif operation == '3':  # Division
            if num2 != 0:
                results = num1 / num2
                return f"Result: {num1} / {num2} = {results}"
            else:
                return "Error: Division by zero is not allowed."
        
        elif operation == '4':  # Multiplication
            results = num1 * num2
            return f"Result: {num1} * {num2} = {results}"
        
        else:
            return "Invalid operation choice."
    
    except ValueError:
        return "Invalid input. Please enter numeric values."


# Main part of the script to get inputs and call the calculator
if __name__ == "__main__":
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    operation = input("Enter the operation number (1/2/3/4): ")
    
    # Call the calculator function and display the result
    result = calculator(num1, num2, operation)
    print(result)
