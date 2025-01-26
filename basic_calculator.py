class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def remainder(self, x, y):
        return x % y

    def power(self, x, y):
        return x ** y

while True:
    print("Please select an operation:")
    print("1- Add")
    print("2- Subtract")
    print("3- Multiply")
    print("4- Divide")
    print("5- Power")
    print("6- Quit")

    try:
        calculator = Calculator()
        user_input = int(input("Please select between (1, 6): "))

        if user_input == 6:
            print("Goodbye!")
            break

        if user_input not in [1, 2, 3, 4, 5]:
            print("Invalid choice! Please select between 1 and 6.")
            continue

        input_x = int(input("Please give a value for x: "))
        input_y = int(input("Please give a value for y: "))

        if user_input == 1:
            result = calculator.add(input_x, input_y)
            print(f"{input_x} + {input_y} = {result}")
        elif user_input == 2:
            result = calculator.subtract(input_x, input_y)
            print(f"{input_x} - {input_y} = {result}")
        elif user_input == 3:
            result = calculator.multiply(input_x, input_y)
            print(f"{input_x} * {input_y} = {result}")
        elif user_input == 4:
            if input_y == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = calculator.divide(input_x, input_y)
                remainder = calculator.remainder(input_x, input_y)
                print(f"{input_x} / {input_y} = {result} with a remainder of {remainder}")
        elif user_input == 5:
            if input_x == 0 and input_y == 0:
                print("Error: X and Y both cannot be zero!")
            else:
                result = calculator.power(input_x, input_y)
                print(f"{input_x} ^ {input_y} = {result}")

    except ValueError:
        print("Invalid input! Please enter a number.")
