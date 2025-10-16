def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return (num1-num2)

def div(num1,num2):
    return num1/num2

print("Welcome to our Calculator")
while True:
    print('Select Operation \n1.Add \n2.Sub \n3.Multi \n.4Division \n5.Average \n.6Exit')
    op=input(('Enter your operation choice(1-6):\t'))
    if(op==6):
        print('Goodbye!')
        break
    if((op>=6) or (op<=0)):
        print('Wrong operation choice only 1 to 6 are allowed')
    else:
    fnum=float(input('Enter first Number: \t'))
    snum=float(input('Enter second Number: \t'))
    if(op==1):
        print(f'Result after adding{fnum},{snum}: \t' ,add(fnum,snum))
    elif(op==2):
        print(f'Result after substracting{fnum},{snum}: \t' ,sub(fnum,snum))
    elif(op==3):
        print(f'Result after multiplying{fnum},{snum}: \t' ,multi(fnum,snum))
    elif(op==4):
        print(f'Result after dividing{fnum},{snum}: \t' ,div(fnum,snum))
    elif(op==5):
        print(f'Average of number{fnum},{snum}: \t' ,avg(fnum,snum))