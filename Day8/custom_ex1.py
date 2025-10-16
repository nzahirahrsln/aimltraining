class InvalidAge(Exception):
    pass

def check_age(age):
    if(age<=0):
        raise InvalidAge('Age should not be negative')
    if(age<18):
        raise InvalidAge('Age should be greater than 18 years')
    if(age>=150):
        raise InvalidAge('Too old for employment')
    else:
        print(f'Age {age}  is accepted and valid age for employment')

    try:
        userage=int(input('Enter your age: '))
        check_age(userage)
    except InvalidAge as inv:
        print('Invalid Age' ,inv)
    except Exception as ex:
        print('Error!!' ,ex)
