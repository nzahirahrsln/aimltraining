from ourpack import wel
username = input('Please Enter your Name: ')
msg=wel.display(username)
print('Message for you: ' ,msg)

from ourpack import student
std1=student.Student(1,'Ali')
std1.displayInfo()