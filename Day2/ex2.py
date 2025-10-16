num=1
print('Printing Numbers from 1 to 100')
while(num<=100):
    print(num,end=" ")
    num+=1

#break example
num=1
print('Print Numbers from 1 to 100 before we get the numbers divisible by 11')
while(num<=100):
    if(num%11==0):
        break
    print(num,end=" ")
    num+=1
#continue example

num=1
while(num<=100):
   
    if(num%11==0):
        num+=1
        continue
    print(num,end="\t")
  
    num+=1


num=1
while(num<=100):
    if(num%5==0):
        num+=1
    
    print(num,end="\t")

    num+=1

for i in range(1,100):
    if(i%5==0):
        continue
    print(i,end="\t")

correctPwd='khays@221'
counter=0
#pwd=input('Enter Password to Start the Game')
#pwd=''
while True:
    pwd=input('Enter Password to Start the Game: \t')
    if(correctPwd==pwd):
        print('Access Granted!!')
        print('**Game started!!**')
        break
    else:    
        print('Wrong Password Entered!!')
        counter+=1
    if(counter>=3):
        print('Blocked for further Attempt!!')
        break
