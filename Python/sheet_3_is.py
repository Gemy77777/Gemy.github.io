# q1
for  i in range(1,11):
    print(i)
    i+=1
# q2
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1,n+1):
    total_sum += i
print("The sum is:", total_sum)
#q3
for i in range(1,21):
    if i % 2 == 0:
        print(i)
# q4
for i in range(10, 0, -1):
    print(i)
#q5
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)
#q6
text = "Python"
count = 0
for char in text:
    count += 1
print(count)

#q7
text = "Hello"
for char in text:
    print(char)
    
#q8
n = 3
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    
#q9
i = 1
while i <= 10:
    print(i)
    i += 1
#q10
total = 0
num = int(input("Enter a number: "))
while num != 0:
    total += num
    num = int(input("Enter a number: "))
print("The sum is:", total)
#q11
count = 1

while count <= 5:
    print("Hello, World!")
    count += 1
#q12
num = 51
while num % 7 != 0:
    num += 1
print(num)

#q13
n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n -= 1
#q14
secret = 2
guess = int(input("Guess a number between 1 and 10: "))
while guess != secret:
    guess = int(input("Wrong, try again: "))
print("Correct! The number was", secret)
#q15
n = 4
result = 1
while n > 0:
    result *= n
    n -= 1
print(result)

#q16
def print_message():
    print("Hello, Python!")
print_message()
#q17
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print(result)
#q18
def find_max(a, b):
    return a if a > b else b
max_value = find_max(10, 20)
print(max_value)
#q19
def calculate_area(length, width):
    return length * width
area = calculate_area(5, 10)
print(area)
#q20
def is_even(n):
    return n % 2 == 0
print(is_even(4))
#q21
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
#q22
def print_range(a, b):
    for i in range(a, b + 1):
        print(i)
print_range(3, 7)
#q23
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))
#q24
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))
#q25
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))
#q26
def square_number(n):
    return n * n
print(square_number(6))
#q27
def generate_multiples(n, count):
    lst = []
    for i in range(1, count + 1):
        lst.append(n * i)
    return lst
print(generate_multiples(3, 5))
#q28
def print_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)
print_pattern(5)
#q29
def celsius_to_fahrenheit(c):
    return (9/5) * c + 32
print(celsius_to_fahrenheit(25))