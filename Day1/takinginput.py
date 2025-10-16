username=input("Enter username ")
age=int(input("Enter age"))
salary=float(input("Enter Salary"))
databaseKn=bool(input("Do you know database?"))

print("Welcome Mr.\\Ms. \t" ,username)
print("Your age is " ,age)
print("Salary is: " ,salary)
print("Know the database " ,databaseKn)


#adding 2 numbers
num1=input(int("Enter first number: \t"))
num2=input(int("Enter second number: \t"))
result=num1+num2
print(f"Result after adding {num1} and {num2} = \t {result}")


#Multiply Two Numbers
num1=input(int("Enter first number: \t"))
num2=input(int("Enter second number: \t"))
result=num1*num2
print(f"Result after multiplication {num1} and {num2} = \t {result}")


#div example
num1=int(input("Enter first number: \t"))
num2=int(input("Enter second number: \t"))
result=num1/num2
print(f"Result after Dividing  {num1} by {num2} = \t {result}")


# % finding Remainder Example
num1=int(input("Enter first number: \t"))
num2=int(input("Enter second number: \t"))
result=num1%num2
print(f"Remainder after Dividing  {num1} by {num2} = \t {result}")


num1=int(input("Enter first number: \t"))
num2=int(input("Enter second number: \t"))
result=int(num1/num2)
print(f"Result after Dividing  {num1} by {num2} = \t {result}")


#taking more than one input using single line
num1,num2=input("Enter two numbers seprated by space").split()

result=int(num1)+int(num2)

print(f"Numbers Entered by you are {num1} and {num2} and addition of numbers {result}")