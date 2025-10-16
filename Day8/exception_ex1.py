try:
    fnum=float(input('Enter First Number: '))
    snum=float(input('Enter Second Number: '))
    result=fnum/snum
    print(f'Result:{result} after dividing {fnum} by {snum}')
except Exception as e:
    print('Error' ,e)
finally:
    print('Good Bye')


