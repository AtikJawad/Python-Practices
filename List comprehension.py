#List Comprehension = A concise way to create lists in Python
#                    Compact and easier to read than traditional Loops

# Basic Syntax : List_name = [Expression for value in iterable if condition ]

#saving double(2x) numbers in a list between 1-10

doubles=[2*x for x in range(1,11)] #range() function is also an iterable 
print(doubles)

#using if condition part 

numbers= [1,2,-3,4,-5,6,7,-8]
positive_num= [num for num in numbers if num>=0]
print(positive_num)

#Inputting via a list comprehension

grades=[int(input("enter values: ")) for x in range(10)]
print(grades)
