# try:
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")
# except ValueError:
#     print(" ent user ebn kalb.")

# #####################################################################################
# try:
#     number = int(input("Enter a number: "))
#     if number > 0:
#         result = sum(range(1, number + 1))
#         print(result)
#     else:
#         print("The number is zero, so the sum is 0.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
    
# #####################################################################################

# try:
#     number = int(input("Enter a number: "))
#     if number > 0:
#         for i in range(1, 11):
#             product = number * i
#             print(f"{number} x {i} = {product}")
#     else:
#         print("Please enter a positive integer greater than 0.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
#######################################################################
'''
vowels = 'aeiouAEIOU'
try:
    text = input('Enter string:')
    count = sum(1 for char in text if char in vowels)
    print(f'Number of vowels: {count}')
except Exception as e:
    print(f'An error occurred: {e}')
    
'''
#######################################################################
# number = int(input("Enter number: "))

# total = 0
# for i in range(1, number + 1):
#     total += i

# print("Sum =", total)



# number = int(input("enter number: "))
# for i in range(1, number+1) :
#     print(i)
    
###########################################################################

# number = int(input("enter number: "))
# for i in range(1,number+1):
#     if i%2 == 0:
#         print(i)
        
###########################################################################
# number = int(input("enter number: "))
# for i in range(1,number+1):
#     if i%2 != 0:
#         print(i)
###########################################################################

'''
number = int(input("enter number: "))
total = 0
for i in range(1,number+1):
    if i%2 !=0:
        total+=i
        
print(f'The sum is {total}')

'''

