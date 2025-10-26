def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            num1 = input("Enter first number (or 'quit' to exit): ")
            if num1.lower() == 'quit':
                break
            
            operator = input("Enter operator (+, -, *, /): ")
            if operator.lower() == 'quit':
                break
            
            num2 = input("Enter second number (or 'quit' to exit): ")
            if num2.lower() == 'quit':
                break
            
            # Convert to numbers
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!\n")
                    continue
                result = num1 / num2
            else:
                print("Error: Invalid operator!\n")
                continue
            
            # Display result
            print(f"Result: {num1} {operator} {num2} = {result}\n")
            
        except ValueError:
            print("Error: Please enter valid numbers!\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()