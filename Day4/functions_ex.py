
def function_name(parameters):
    '''Docstring'''
    statement(s)

#function without parameters
def welcome():
    print("Welcome to Functions")
    print("Our First function ")

welcome()
#function with a parameter
def welcome(n):
    print("Welcome to functions in python Mr.\\Ms",n)

username=input('Enter your name: \t')
# #function
welcome(username)

# function with parameter and return

def add(num1,num2):
    return num1+num2

fnum=int(input("Enter first Number: \t"))
snum=int(input("Enter second Number: \t"))
print(f'Result after adding {fnum} and {snum} is =\t',add(fnum,snum))

def multi(num1,num2):
    return num1*num2

fnum=int(input("Enter first Number: \t"))
snum=int(input("Enter second Number: \t"))
print(f'Result after multiplying {fnum} and {snum} is =\t',multi(fnum,snum))