# function

#  def function_name(param1,param2,.....paramn):

    # function definition

    # return value

# def add (num1,num2) :

#     result = num1 + num2

#     return result

# print(add(20,40))

# def is_Odd (num1) :

#     result = True if num1 % 2 == 0 else False

#     return result

# print(is_Odd(12))

# def max_Two (num1,num2) :

#     result = num1 if num1 > num2 else num2

#     return result

# print(max_Two(10,48))

# def cube (num) :

#     result = num**3

#     return result

# print(cube(3))

def is_leap_year (year) :

    if year % 400 == 0 and  (year % 100 != 0 or year % 4 == 0) :

        return True
    
    else :

        return False

print(is_leap_year(2023))

print(is_leap_year(2020))

print(is_leap_year(2898))