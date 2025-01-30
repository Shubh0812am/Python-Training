
# day 1

# java c c++
# int num = 10;

# python 
# num = 10 

# eid = 101
# first_name = 'Sonu'
# salary = 10.25

# print(eid, first_name, salary)

# camelCase 
# PascleCase 
# snake_case 

# identifier -  C++           python 
# class name -  ClassName     ClassName  
# method name - methodName    method_name function_name 
# field name - fildName       field_name 
# file name - SameAsClassName.java file-name.py 
# package name  - package.name packagename 
# a op          /              // 




# program to add two integers and print the sum , three vriables 

# arithmetic operators in python 
# ------------------------------
# print(10 + 2)
# print(10 - 2)
# print(10 / 2)
# print(10 * 2)
# print(10 % 2) # example 

# // ** 

# print(10 / 3)
# print(10 // 3)

# print (2 * 2)
# print (2 ** 2)

# print (2 * 3)
# print (2 ** 3)

# C++ 
# num++ num--
# ++num --num

# num = 10
# print(num)
# # num++ 
# num += 1
# print(num)

# comparison / relational operartors 
# ---------------------------------- 

#  == != > >= < <= 

# a, b, c = 10, 5, 8
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)

# logical operators 

#  && and || or ! not 

# # if (a > b && b < c):
# if a > b and b < c:
#     print('yes')
# else: 
#     print('no')

#  assignment operators 

#  = += -= *= /= //= **= %= 

# num = 10
# print(num)
# num += 1
# print(num)
# num *= 2
# print(num)

# identity operators 
#  is is not 

# x = [10, 20, 30]
# y = x 
# z = [10, 20, 30]

# print( x is y)
# print( x == y)
# print( x is z)
# print( x == z)
# print(x is z)
# print(x is not z)


# advanded data types
# list [], dictionary, tuple (), set, obejct of class 

# my_list = [10, 'abc', False, 10, 20] # ordered 
# print(my_list)

# # print(my_list[2])

# # for i in my_list:
# #     print(i)

# my_set = {20, 10, 50, 30, 40} # unrodered 

# print(my_set)

# control statements 
# if if else if elif 
# loops 

a, b = 5, 5

# if a > b:
#     print(a > b)
# else:
#     print( a, b)
    
# if a > b:
#     print(a > b)
# elif a < b:
#     print( a < b)
# else: 
#     print('other case')


# loops 

# # while loop 

# count = 1

# while count <= 5:
#     print(count)
#     count += 1

#  for loop 
# employees = ['Sonu', 'Monu', 'Tonu', 'Sona']

# for emp in employees:
#     print(emp)

#  range 
# for i in range(1, 5):
#     print(i)

# emp_details = {'eid': 101, 'name': 'Sonu', 'salary': 10.25, 'phone': 9876543210, 'city': 'Pune'}

# for key, value in emp_details.items():
#     if key == 'salary':
#         continue
#         # break
#         # pass # like a placeholder 
#     print(key, value)
    
# # nested loop 

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j)

#  write a program to find berth type based on berth number in indian railway 3A coaches 
# 1 - 72 
# lower, middle, upper, sidelower, sideupper
# berth_number = 1 # input 
# type_of_berth = 'lower' # output 

# berth_number = int(input('Please enter your berth number 1 - 72'))
berth_number = 22 # input 
if berth_number >= 1 and berth_number <= 72:
    print(berth_number)
    if berth_number % 8 == 1 or berth_number % 8 == 4:
        print('lower')
    elif berth_number % 8 == 2 or berth_number % 8 == 5:
        print('middle')
    elif berth_number % 8 == 3 or berth_number % 8 == 6:
        print('upper')
    elif berth_number % 8 == 7:
        print('sidelower')
    elif berth_number % 8 == 0:
        print('sideupper')
else:
    print('invalid berth number')