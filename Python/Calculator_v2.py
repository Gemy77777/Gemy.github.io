import math
import numpy as np

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
    """Handles general mathematical operations using numpy arrays for performance."""

    def __init__(self):
        self.numbers1 = np.array([])
        self.numbers2 = np.array([])
        self.operator = ""

    def get_numbers(self, prompt):
        """Prompts user for numbers and returns them as a numpy array of floats."""
        nums = input(prompt)
        if nums.strip() == "":
            return np.array([])
        return np.array([float(num) for num in nums.split()])

    def get_operator(self):
        """Prompts user for the operator."""
        return input("Enter operator: ").strip().lower()

    def calculate(self):
        """Performs the calculation based on user input using numpy arrays."""
        self.numbers1 = self.get_numbers("Enter the first number(s), separated by space: ")
        self.operator = self.get_operator()
        if self.operator in ["+", "-", "*", "/", "^", "%", "p%", "divmod"]:
            self.numbers2 = self.get_numbers("Enter the second number(s), separated by space: ")
        else:
            self.numbers2 = np.array([])

        try:
            if self.operator == "+":
                result = np.sum(np.concatenate((self.numbers1, self.numbers2)))
            elif self.operator == "-":
                if self.numbers2.size > 0:
                    result = np.subtract(self.numbers1, self.numbers2)
                else:
                    result = np.diff(self.numbers1)
            elif self.operator == "*":
                result = np.prod(np.concatenate((self.numbers1, self.numbers2)))
            elif self.operator == "/":
                if self.numbers2.size > 0:
                    result = np.divide(self.numbers1, self.numbers2)
                else:
                    result = np.divide.reduce(self.numbers1)
            elif self.operator == "^":
                if self.numbers2.size > 0:
                    result = np.power(self.numbers1, self.numbers2)
                else:
                    result = np.power.reduce(self.numbers1)
            elif self.operator == "%":
                if self.numbers1.size == 1 and self.numbers2.size == 1:
                    result = (self.numbers1[0] / self.numbers2[0]) * 100
                    print(f"{result}%")
                    return
                else:
                    print("Percentage requires one number in each set.")
                    return
            elif self.operator == "p%":
                if self.numbers1.size == 1 and self.numbers2.size == 1:
                    result = self.numbers1[0] * (self.numbers2[0] / 100)
                else:
                    print("Percentage of a number requires one number in each set.")
                    return
            elif self.operator == "min":
                result = np.min(self.numbers1)
            elif self.operator == "max":
                result = np.max(self.numbers1)
            elif self.operator == "sqrt":
                result = np.sqrt(self.numbers1)
            elif self.operator == "app.":
                result = round(np.mean(self.numbers1))
            elif self.operator == "sin":
                result = np.round(np.sin(np.radians(self.numbers1)), 2)
            elif self.operator == "cos":
                result = np.round(np.cos(np.radians(self.numbers1)), 2)
            elif self.operator == "tan":
                result = np.round(np.tan(np.radians(self.numbers1)), 2)
            elif self.operator == "deg to rad":
                result = np.radians(self.numbers1)
            elif self.operator == "rad to deg":
                result = np.degrees(self.numbers1)
            elif self.operator == "!":
                if self.numbers1.size == 1 and self.numbers1[0] >= 0 and self.numbers1[0].is_integer():
                    result = math.factorial(int(self.numbers1[0]))
                else:
                    print("Factorial requires a single non-negative integer.")
                    return
            elif self.operator == "log_10":
                result = np.log10(self.numbers1[self.numbers1 > 0])
            elif self.operator == "log":
                result = np.log(self.numbers1[self.numbers1 > 0])
            elif self.operator == "abs":
                result = np.abs(self.numbers1)
            elif self.operator == "divmod":
                if self.numbers1.size == 1 and self.numbers2.size == 1:
                    result = divmod(int(self.numbers1[0]), int(self.numbers2[0]))
                else:
                    print("Divmod requires one number in each set.")
                    return
            elif self.operator == "sort":
                result = np.sort(self.numbers1)
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
            if continue_or_not.lower() == "e":
                print('Quitting... Goodbye!')
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