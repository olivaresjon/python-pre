# Q1) Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print('hello_USERNAME!')
hello_name('user_name')

# Q2) Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for numbers in range(1,100):
        if numbers % 2 != 0:
            print(numbers)
    return
first_odds()

# Q3) Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    digits = [1,10,5,96,13,22]
    print("the biggest number in the list is: ", max(digits))
max_num_in_list('a_list')

# Q4) Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
def is_leap_year(year):
    leap = False
    if year % 400 == 0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
# the 'return' in line 32 will give the output of 'leap' in line 26
    return leap
#2022 is not a leap year but 2020 is
year = int(2022) 
print(is_leap_year(year))

# question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# I need help to solve this problem (tried google)

