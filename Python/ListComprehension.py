# the golden rule -> [expression for item in iterable if condition]

# example 1
# squares = [x*x for x in range(1,11)]
# print(squares)

# example 2

even_num = [100, 101, 102, 103, 104, 105]

even_num = [num for num in even_num if num%2 == 0]
print(even_num)