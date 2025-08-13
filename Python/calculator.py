while True:
    try:   
        import math
        continue_or_not = input("press Enter to continue or end to exit: ")
        if continue_or_not == "end":
            print('ok.. bye bye<3')
            break
        else:
            pass
        operator = input("Enter operator: ")
        if operator == "end":
            print('ok.. bye <3')
            break
        elif operator == "min":
            input ("this function choosing the smallest num\n press any key to continue ")
        elif operator == "max":
            input("this function choosing the smallest num\n press any key to continue")
        elif operator == "app":
            input("this function makes approximation\n press any key to continue")
        elif operator == "sqrt":
            input("this function makes square root\n press any key to continue")
        elif operator == "rad to deg":
            input("this function convert radian to degree\n press any key to continue")
        elif operator == "deg to rad":
            input("this function convert degree to radian\n press any key to continue")
        else:
            pass

        numbers = [float(num) for num in input("Enter numbers separated by space: ").split()]
        try:
            pass
        except ValueError:
            print("Please enter valid numbers.")
            exit()

        if operator == "+":
            result = sum(numbers)
            print(result)
        
        elif operator == "-":
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print(result)       
        elif operator == "*": 
            result = 1
            for num in numbers:
                result *= num
            print(result)
        elif operator == "/":
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
            print(result)
        elif operator == "^":
            result = numbers[0]
            for num in numbers[1:]:
                result **= num  
            print(result)
        elif operator == "app.": # approximation
            result = round(sum(numbers) / len(numbers))
            print(result)
        elif operator == "max":# Maximum number
            result = max(numbers)
            print(result)
        elif operator == "min":#Minimum number
            result = min(numbers)
            print(result)

        elif operator == "%":
            if len(numbers) != 2:
                print("percentage requires exactly two numbers")
            else:
                result = (numbers[0] / numbers[1]) * 100
                print(f"{result}%") 
                
        elif operator == "p%": 
            if len(numbers) != 2:
                print("Percentage of a number operation requires exactly two numbers.")
            else:
                result = numbers[0] * (numbers[1] / 100)
                print(result)
        elif operator == "sqrt": # squaring 
            result = numbers[0]
            for num in numbers[0:]:
                result = math.sqrt(num)     
            print(result)
        elif operator == "sin":
            result = numbers[0]
            for num in numbers[0:]:
                result = [round(math.sin(math.radians(num)),1)]
            print(result)
        elif operator == "cos":
            result = numbers[0]
            for num in numbers[0:]:
                result = [round(math.cos(math.radians(num)),1)]
            print(result)
        elif operator == "tan":
            result = numbers[0]
            for num in numbers[0:]:
                result = [round(math.tan(math.radians(num)),1)]
            print(result)
        elif operator == "sec":
            result = numbers[0]
            for num in numbers[0:]:
                result = [1/round(math.sin(math.radians(num)),1)]
            print(result)    
        elif operator == "csc":
            result = numbers[0]
            for num in numbers[0:]:
                result = [1/round(math.cos(math.radians(num)),1)]
            print(result)
        elif operator == "cot":
            result = numbers[0]
            for num in numbers[0:]:
                result = [1/round(math.tan(math.radians(num)),1)]
            print(result)
        elif operator == "!":
            if len(numbers) != 1 or numbers[0] < 0:
                print("Factorial function requires a non-negative integer.")
            else:
                result = math.factorial(int(numbers[0]))
                print(result)
        elif operator == "log_10":
            numbers = [int(num) for num in numbers]
            result = numbers[0]
            for num in numbers[0:]:
                result = math.log10(numbers[0])
            print(result)
        elif operator == "log":
            numbers = [float(num) for num in numbers]
            if len(numbers) != 1 or numbers[0] <= 0:
                print("Logarithm function requires exactly one +ve number.")
            else:
                result = math.log(numbers[0])
                print(result)
        elif operator == 'abs':
            result = numbers[0]
            for num in numbers:
                result = abs(numbers[0])
            print('the absolute number=', result)
        elif operator == 'divmod':
            numbers = [int(num) for num in numbers]
            result = numbers[0]
            for num in numbers[0:]:
                result = divmod(numbers[0], numbers[1])
            print(result)
        elif operator == 'sort':
            numbers = [int(num) for num in numbers]
            result = numbers[0]
            for num in numbers[0:]:
                result = sorted(numbers)
            print(result)
                                    
        #Angular Conversion
        elif operator == "deg to rad":
            result = math.radians(numbers[0])
            print(result)
        elif operator == "rad to deg":
            result = math.degrees(numbers[0])
            print(result)
        else:
            print("invalid operator.. please try again")      
            
    except ValueError:
        print('Invalid input... Please try again')
    except Exception:
        print('Unknown Error.. Please try again')