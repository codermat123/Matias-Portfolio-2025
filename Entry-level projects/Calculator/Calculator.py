def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y if y != 0 else "Cannot divide by zero"

def power(x, exponent):
    return x ** exponent

def calculator ():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentation")

    choice = input("Select operation (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            num = float(input("Enter a number: "))
            exponent = float(input("Enter the exponent: "))
            result = power(num, exponent)
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                 result = divide(num1, num2)

        print("Result: ", result)

    else:
        print("Invalid Input")

calculator()
        

