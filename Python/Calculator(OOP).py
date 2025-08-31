import math
class ShapeCalculator:
    """Handles area calculations for various shapes."""
    @staticmethod
    def calculate_area():
        """Prompts user for shape and calculates its area."""
        print("Available shapes: circle, square, rectangle, triangle, parallelogram, trapezoid")
        shape = input("Enter the shape: ").strip().lower()
        if shape in ("circle", "c"):
            r = float(input("Enter the radius: "))
            area = math.pi * r * r
            print(f"Area of circle: {area:.2f}")
        elif shape in ("square", "s"):
            a = float(input("Enter the side length: "))
            area = a * a
            print(f"Area of square: {area:.2f}")
        elif shape in ("rectangle", "r"):
            l = float(input("Enter the length: "))
            w = float(input("Enter the width: "))
            area = l * w
            print(f"Area of rectangle: {area:.2f}")
        elif shape in ("triangle", "t"):
            b = float(input("Enter the base: "))
            h = float(input("Enter the height: "))
            area = 0.5 * b * h
            print(f"Area of triangle: {area:.2f}")
        elif shape in ("parallelogram", "p"):
            b = float(input("Enter the base: "))
            h = float(input("Enter the height: "))
            area = b * h
            print(f"Area of parallelogram: {area:.2f}")
        elif shape in ("trapezoid",):
            a = float(input("Enter the first base: "))
            b = float(input("Enter the second base: "))
            h = float(input("Enter the height: "))
            area = 0.5 * (a + b) * h
            print(f"Area of trapezoid: {area:.2f}")
        else:
            print("Unknown shape.")
class Calculator:
    """Handles general mathematical operations."""
    def __init__(self):
        self.numbers1 = []
        self.numbers2 = []
        self.operator = ""
    def get_numbers(self, operator):
        """Prompts user for numbers and returns them as a list of floats."""
        return [float(num) for num in input(operator).split()]
    def get_operator(self):
        """Prompts user for the operator."""
        return input("Enter operator: ").strip().lower()
    def calculate(self):
        """Performs the calculation based on user input."""
        self.numbers1 = self.get_numbers("Enter the first number(s), separated by space: ")
        self.operator = self.get_operator()
        if self.operator in ["+", "-", "*", "/", "^", "%", "p%", "divmod"]:
            self.numbers2 = self.get_numbers("Enter the second number(s), separated by space: ")
        else:
            self.numbers2 = []
        try:
            if self.operator == "+":
                result = sum(self.numbers1 + self.numbers2)
            elif self.operator == "-":
                result = self.numbers1[0]
                for num in self.numbers1[1:] + self.numbers2:
                    result -= num
            elif self.operator == "*":
                result = 1
                for num in self.numbers1 + self.numbers2:
                    result *= num
            elif self.operator == "/":
                result = self.numbers1[0]
                for num in self.numbers1[1:] + self.numbers2:
                    result /= num
            elif self.operator == "^":
                result = self.numbers1[0]
                for num in self.numbers1[1:] + self.numbers2:
                    result **= num
            elif self.operator == "%":
                if len(self.numbers1) == 1 and len(self.numbers2) == 1:
                    result = (self.numbers1[0] / self.numbers2[0]) * 100
                    print(f"{result}%")
                    return
                else:
                    print("Percentage requires one number in each set.")
                    return
            elif self.operator == "p%":
                if len(self.numbers1) == 1 and len(self.numbers2) == 1:
                    result = self.numbers1[0] * (self.numbers2[0] / 100)
                else:
                    print("Percentage of a number requires one number in each set.")
                    return
            elif self.operator == "min":
                result = min(self.numbers1)
            elif self.operator == "max":
                result = max(self.numbers1)
            elif self.operator == "sqrt":
                result = [math.sqrt(num) for num in self.numbers1]
            elif self.operator == "app.":
                result = round(sum(self.numbers1) / len(self.numbers1))
            elif self.operator == "sin":
                result = [round(math.sin(math.radians(num)), 2) for num in self.numbers1]
            elif self.operator == "cos":
                result = [round(math.cos(math.radians(num)), 2) for num in self.numbers1]
            elif self.operator == "tan":
                result = [round(math.tan(math.radians(num)), 2) for num in self.numbers1]
            elif self.operator == "deg to rad":
                result = [math.radians(num) for num in self.numbers1]
            elif self.operator == "rad to deg":
                result = [math.degrees(num) for num in self.numbers1]
            elif self.operator == "!":
                if len(self.numbers1) == 1 and self.numbers1[0] >= 0 and self.numbers1[0].is_integer():
                    result = math.factorial(int(self.numbers1[0]))
                else:
                    print("Factorial requires a single non-negative integer.")
                    return
            elif self.operator == "log_10":
                result = [math.log10(num) for num in self.numbers1 if num > 0]
            elif self.operator == "log":
                result = [math.log(num) for num in self.numbers1 if num > 0]
            elif self.operator == "abs":
                result = [abs(num) for num in self.numbers1]
            elif self.operator == "divmod":
                if len(self.numbers1) == 1 and len(self.numbers2) == 1:
                    result = divmod(int(self.numbers1[0]), int(self.numbers2[0]))
                else:
                    print("Divmod requires one number in each set.")
                    return
            elif self.operator == "sort":
                result = sorted(self.numbers1)
            elif self.operator == "is even":
                for num in self.numbers1:
                    if num % 2 == 0:
                        print(f"{num} is even.")
                    else:
                        print(f"{num} is odd.")
                return
            else:
                print("Invalid operator. Please try again.")
                return
            print(result)
        except Exception as exc:
            print(f"Calculation error: {exc}")
def main():
    """Main loop for the calculator program."""
    while True:
        try:
            continue_or_not = input("Press Enter to continue or 'e' to exit: ")
            if continue_or_not == "e" or continue_or_not == "E":
                print('Ok.. Bye Bye')
                break
            area_choice = input("Do you want to calculate the area of a shape? (y/n): ").strip().lower()
            if area_choice == "y":
                ShapeCalculator.calculate_area()
                continue
            calc = Calculator()
            calc.calculate()
        except ValueError:
            print('Invalid input... Please try again')
        except Exception as e:
            print(f'Unknown Error: {e} ... Please try again')
if __name__ == "__main__":
    main()