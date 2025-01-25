class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

while True:
    print("Please select an operation:")
    print("1- Add")
    print("2- Subtract")
    print("3- Multiply")
    print("4- Divide")
    print("5- Quit")

    try:
        calculator = Calculator()
        user_input = int(input("Please select between (1, 5): "))

        if user_input == 5:
            print("Goodbye!")
            break

        if user_input not in [1, 2, 3, 4]:
            print("Invalid choice! Please select between 1 and 5.")
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
                print(f"{input_x} / {input_y} = {result}")

    except ValueError:
        print("Invalid input! Please enter a number.")
