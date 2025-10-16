# import random

# print('Random Number from 1 to 1000')

# print(random.randint(1,10))

import random
def findwinner():
    name=input('Enter Your name: ')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr.\\Ms { name} Cuppon Number: {luckyNumber}')
    if(luckyNumber==2):
        print('you have won Perodua Myvi Car')
    elif(luckyNumber==4):
        print('you have won an IPad')  
    elif(luckyNumber==5):   
      print('you have won an IPhone')  
    else:
        print('Better Luck Next Time') 