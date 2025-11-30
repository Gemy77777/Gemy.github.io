#Q1
list = ['cairo', 'alex', 'giza', 'aswan', 'luxor']
print(list)

#Q2
list = ['cairo', 'alex', 'giza', 'aswan', 'luxor']
print(list[0], list[-1])

# Q3
list = ['cairo', 'alex', 'giza', 'aswan', 'luxor']
print("Current list:", list)
list[1] = input("Enter a new city name: ")
print("Updated list:", list)

#Q4
list = [10, 20, 30, 40, 50]
print(len(list))

# Q5
list = [10, 20, 30, 40]
print(sum(list))

# Q6
list = [10, 20, 30, 40, 50]
print(max(list))

# Q7
list = [10, 20, 30, 40, 50]
print(list[::-1])

# Q8
list = [10, 20, 30, 40, 40, 50, 50]
print(set(list))

# Q9
list1 = [100, 20, 10, 50 , 5]
print(sorted(list1))

# Q10
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# Q11
tuple = ("cairo", "alex", "giza", "aswan", "luxor")
print(tuple)

# Q12
tuple = ("cairo", "alex", "giza", "aswan", "luxor")
print(tuple[0], tuple[-1])

# Q13
tuple = ("cairo", "alex", "giza", "aswan", "luxor")
if "cairo" and "alex" and "luxor" in tuple:
    print("Found")
else:
    print("Not Found")

#Q14
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80)
print(tuple1 + tuple2)

#Q15
tuple = (10, 20, 30, 40, 50)
tuple = list(tuple)
print(tuple)

# Q16
tuple = (10, 20, 30, 40, 50)
print(len(tuple))

# Q17
tuple = (10, 20, 30)
a = tuple[0]
b = tuple[1]
c = tuple[2]
print(a, b, c)

#Q18
set = {10, 20, 30, 40, 50}
print(set)

#Q19
set = {10, 20, 30, 40, 50}
set.add(60)
print(set)

#Q20
set = {10, 20, 30, 40, 50}
print("Current set:", set)
i = int(input("Enter a number to search: "))
if i in set:
    set.remove(i)
    print("Found and Removed")
    print(set)
else:
    print("doesn't exist")
    

#Q21
list = [10, 20, 30, 40, 50]
print(set(list))

# Q22
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("UNion = ",set1.union(set2))
print("Intersection = ", set1.intersection(set2))
print("Difference = ", set1.difference(set2))

