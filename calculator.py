# This project will include making a simple calculator. Implementing addition, subtraction, multiplication, and division operations.
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2 
def divide(num1, num2):
    if num2 ==0:
        return "Error: Can't divide by zero"
    return num1 / num2

def main():
    while True:
        print("Calculator Options: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a number: "))
            result = add(num1, num2)
            print("Result:", result)

        elif choice =='2':
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a number: "))
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice =='3':
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a number: "))
            result = divide(num1, num2)
            print("Result:", result)

        elif choice =='4':
            num1 = float(input("Input a number: "))
            num2 = float(input("Input a number: "))
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice =='5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 10.")

if __name__== "__main__":
    main()
    