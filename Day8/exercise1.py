# Take user marks from user with in 0 to 50
# If user enter out of range [0-50] raise Error invalidmarks using custom exception
# Give chance to the user till, she entered valid marks

class InvalidMarks(Exception):
    pass

def check_marks(marks):
    while True:
        try:
            if(marks<0 or marks>50):
                raise InvalidMarks('Invalid Marks Entered!')
            else:
                marks = int(input('Enter your marks: \t'))
                print(f'Marks Accepted!')

        except ValueError as e:
            print('Error in values! Please Enter Numbers!')

        except InvalidMarks as iv:
            print('Invalid Marks' ,iv)

#-----------------------------------------------------
#from sir
#from ourpack import mark

class InvalidMarks(Exception):
    pass

def check_marks(marks):
    if(marks<0):
        raise InvalidMarks('Marks cannot be negative')
    elif(marks>50):
        raise InvalidMarks('Marks should be within range 0-50 only')
    else:
        print(f'Marks {marks} is accepted!')

while True:
    try:
        usermarks=int(input('Enter your marks [0-50]: '))
        check_marks(usermarks)
    except InvalidMarks as inv:
        print('Invalid Marks Entered!' ,inv)
    except Exception as ex:
        print('Error!!' ,ex)
    else:
        print('Recorded')
        break
    choice=input('Do you want to re-enter marks? If yes press y: \t').lower()
    if(choice!=y):
        print('Bye')
        break