#Colin Taylor
#Assignement 5
#this funtion program computs many differrent math operations
class BasicMathOperations:

    def greet_user(self, first, last):
        #combines the first and last name inputs of the user
        full_name = f"{first} {last}"
        return f"Welcome to math operations, {full_name}"

    def add_numbers(self):
        
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1 + num2
    

    def perform_operation(self, num1, num2, operator):
            # pefomrs the operation of the two numbers based on the argument input
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "Error: Division by zero"
                else:
                    return num1 / num2
            else:
                return "that is not an operator"

    def square_number(self, number):
            #squares the number
            return number ** 2
    

    def factorial(self, num):
       
            factorial = 1
            # error handling for a number less than 0
            if num < 0:
                return "Error:please only use positive numbers"
            #for the range of the number i it mulitplies the number by i each time through the loop
            for i in range(1, num + 1):
                factorial *= i
            return factorial
        

    def counting(self, start, end):
        # iterates through the start to the end and prints out each point in between
            for i in range(start, end + 1):
                print(i, end=' ')
            print() 

 

    def calculate_hypotenuse(self, s1, s2):
       #uses calculate sqauare method for each side of triangle then takes the square root of it
            hypotenuse = (self.square_number(s1) + self.square_number(s2)) ** 0.5
            return hypotenuse

    def area_of_rectangle(self, width, height):
            # error handling of negative numbers
            if width <= 0 or height <= 0:
                return "Error, Width and height must be positive."
            return width * height
      
# just raises the number to the exponent
    def power_of_number(self, num, exponent):
       
            return num ** exponent
    

    def type_of_argument(self, arg):
       
            return type(arg)

def main():
    #create instanace of class
    math = BasicMathOperations()

    #welcome the user
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print(math.greet_user(first,last))
    #displays the options
    print("please pick the number of the choice you would like to do")
    print("1: Add Numbers")
    print("2: Perform Operation")
    print("3: Square Number")
    print("4: Factorial")
    print("5: Counting")
    print("6: Calculate Hypotenuse")
    print("7: Area of Rectangle")
    print("8: Power of Number")
    print("9: Type of Argument")

    choice = input("Enter the number of the operation you want to perform: ")

    #runs methods based on choice of user
    if choice == '1':
        result = math.add_numbers()
        print("Sum:", result)
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        result = math.perform_operation(num1, num2, operator)
        print("Result:", result)
    elif choice == '3':
        number = float(input("Enter a number: "))
        result = math.square_number(number)
        print("Square:", result)
    elif choice == '4':
        number = int(input("Enter a number: "))
        result = math.factorial(number)
        print("Factorial:", result)
    elif choice == '5':
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        math.counting(start, end)
    elif choice == '6':
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        result = math.calculate_hypotenuse(side1, side2)
        print("The Hypotenuse is", result)
    elif choice == '7':
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        result = math.area_of_rectangle(width, height)
        print("The Area of the Rectangle is", result)
    elif choice == '8':
        base = float(input("Enter the base number: "))
        exponent = float(input("Enter the exponent: "))
        result = math.power_of_number(base, exponent)
        print("The Power of the number is", result)
    elif choice == '9':
        argument = input("Enter an argument: ")
        result = math.type_of_argument(argument)
        print("The argument type is", result)
    else:
        print("error: Please enter a number between 1 and 9.")


main()