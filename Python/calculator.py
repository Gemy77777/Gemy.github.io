import math
while True:
    try:
        continue_or_not = input("Press Enter to continue or 'e' to exit: ")
        if continue_or_not == "e":
            print('Ok.. Bye Bye')
            break
        # Get the first set of numbers
        numbers1 = [float(num) for num in input("Enter the first number(s), separated by space: ").split()]
        operator = input("Enter operator: ").strip().lower()
        # For operators that need a second set of numbers
        if operator in ["+", "-", "*", "/", "^", "%", "p%", "divmod"]:
            numbers2 = [float(num) for num in input("Enter the second number(s), separated by space: ").split()]
        else:
            numbers2 = []
        # Perform calculation
        if operator == "+":
            result = sum(numbers1 + numbers2)
            print(result)
        elif operator == "-":
            result = numbers1[0]
            for num in numbers1[1:] + numbers2:
                result -= num
            print(result)
        elif operator == "*":
            result = 1
            for num in numbers1 + numbers2:
                result *= num
            print(result)
        elif operator == "/":
            result = numbers1[0]
            for num in numbers1[1:] + numbers2:
                result /= num
            print(result)
        elif operator == "^":
            result = numbers1[0]
            for num in numbers1[1:] + numbers2:
                result **= num
            print(result)
        elif operator == "%":
            if len(numbers1) == 1 and len(numbers2) == 1:
                result = (numbers1[0] / numbers2[0]) * 100
                print(f"{result}%")
            else:
                print("Percentage requires one number in each set.")
        elif operator == "p%":
            if len(numbers1) == 1 and len(numbers2) == 1:
                result = numbers1[0] * (numbers2[0] / 100)
                print(result)
            else:
                print("Percentage of a number requires one number in each set.")
        elif operator == "min":
            result = min(numbers1)
            print(result)
        elif operator == "max":
            result = max(numbers1)
            print(result)
        elif operator == "sqrt":
            result = [math.sqrt(num) for num in numbers1]
            print(result)
        elif operator == "app.":
            result = round(sum(numbers1) / len(numbers1))
            print(result)
        elif operator == "sin":
            result = [round(math.sin(math.radians(num)), 2) for num in numbers1]
            print(result)
        elif operator == "cos":
            result = [round(math.cos(math.radians(num)), 2) for num in numbers1]
            print(result)
        elif operator == "tan":
            result = [round(math.tan(math.radians(num)), 2) for num in numbers1]
            print(result)
        elif operator == "deg to rad":
            result = [math.radians(num) for num in numbers1]
            print(result)
        elif operator == "rad to deg":
            result = [math.degrees(num) for num in numbers1]
            print(result)
        elif operator == "!":
            if len(numbers1) == 1 and numbers1[0] >= 0 and numbers1[0].is_integer():
                result = math.factorial(int(numbers1[0]))
                print(result)
            else:
                print("Factorial requires a single non-negative integer.")
        elif operator == "log_10":
            result = [math.log10(num) for num in numbers1 if num > 0]
            print(result)
        elif operator == "log":
            result = [math.log(num) for num in numbers1 if num > 0]
            print(result)
        elif operator == "abs":
            result = [abs(num) for num in numbers1]
            print(result)
        elif operator == "divmod":
            if len(numbers1) == 1 and len(numbers2) == 1:
                result = divmod(int(numbers1[0]), int(numbers2[0]))
                print(result)
            else:
                print("Divmod requires one number in each set.")
        elif operator == "sort":
            result = sorted(numbers1)
            print(result)
        elif operator == "is even":
            for num in numbers1:
                if num % 2 == 0:
                    print(f"{num} is even.")
                else:
                    print(f"{num} is odd.")
        else:
            print("Invalid operator. Please try again.")
    except ValueError:
        print('Invalid input... Please try again')
    except Exception as e:
        print(f'Unknown Error: {e} ... Please try again')