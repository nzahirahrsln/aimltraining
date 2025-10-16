def factorial(num):
    if((num==0) or (num==1)):
        return 1
    else:
        return num*factorial(num-1)


num=int(input('Enter a number to find out factorial: '))
print(f'Factorial of {num} is: ' ,factorial(num))

# Write a python function which converts inches to cms.
# 1inch = 2.5cm
def conv_inch_cm(inches):
    cm = inches * (2.5)
    return inches

num=int(input('Enter a number to convert inches to cm: '))
print(f'Inches{inches}')

#correct answer
def conv_inch_cm(num):
    return num*2.5

num=int(input('Enter inches: '))
print(f'{num} inches are equal to {conv_inch_cm(num)} cm')

# Write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter Number to findout table'))
gen_table(number)


def display():
    print('Welcome to recap of functions')

def welcome(name):
    print('Welcome to functions Mr.\\Ms.',name)

def cube(num):
   cube_num=num*num*num
   print(f'Cube of given Number: {num} is =\t {cube_num}')

def square(num):
   sq_num= num*num
   print(f'Squar of given Number: {num} is =\t {sq_num}')
  

# def salBonus(salary):
#     return salary*0.10

# welcome('sam')    
# display() 
# my_num=int(input('Enter Number to find out Cube:\t')) 
# cube(my_num)  
# username=input('Enter User Name: \t')
# my_num=int(input('Enter number to find out cube and square: \t'))
# welcome(username)
# cube(my_num)
# square(my_num)


# sq=square(my_num)
# print(f'Square of {my_num} is: {sq}')
# print(f'Number: {my_num} Square: {sq}')
# my_sal=float(input('Enter Salary to find out bonus: \t'))
# bonus=salBonus(my_sal)
# print(f'Salary {my_sal} Bonus: {bonus}')
# print(f'Salary after bonus =\t',(my_sal+bonus))

def salBonus(salary):
    bonus=salary*0.10
    print(f'Salary {salary} Bonus: {bonus}')

my_sal=float(input('Enter Salary to find out bonus: \t'))
salBonus(my_sal)  
#print(f'Salary after bonus =\t')  