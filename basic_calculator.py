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
    print("""What do you want with x,y values?
1- Add
2- Subtract
3- Multiply
4- Divide
5- Quit""")

    try:
        calculator = Calculator()
        user_input = int(input("Please select between (1, 5): "))
        if user_input == 5:
            print("Goodbye!")
            break
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
            result = calculator.divide(input_x, input_y)
            print(f"{input_x} / {input_y} = {result}")
    except ValueError:
        print("Invalid input! Please enter a number.")
