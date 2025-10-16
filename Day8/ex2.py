from ourpack import calc
while True:
    try:
        fnum=float(input('Enter First Number: '))
        snum=float(input('Enter Second Number: '))
        op=input('Choose operation +,-,*,/')    

        if(op=='+'):
            print('Result: \t' ,calc.add(fnum,snum))
        elif(op=='-'):
            print('Result: \t' ,calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result: \t' ,calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result: \t' ,calc.div(fnum,snum))
        else:
            #print('Wrong operation Choice')
            raise ValueError
        
    except ZeroDivisionError as ze:
        print('Divison by 0 is not allowed' ,ze)
    except ValueError as ve:
        print('Error in Values' ,ve)
    except Exception as ex:
        print('Error!!',ex)
    # finally:
    #     print('End of Program')
choice=input('Do you want to continue? If yes press y: \t').lower()
if(choice!='y'):
    print('Bye')
    #break