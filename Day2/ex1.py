print("0 to 9 \n")
for i in range(10):
    print(i)

print("First Example")
for i in range(10):
    print(i)
    print("Welcome")

print("Second Example")
for i in range(1,11):
    print(i)

print("Third Example")
for i in range(10):
    print(i+1)

for i in range(5):
    print(i)

for i in range(3,5):
    print(i)

for item in range(100):
    print(item+1, end=" \t")

employees=['Raj', 'Ravi', 'Sam', 'Ali', 'Abu']
for e in employees:
    print(e)

products=['FaceWash', 'Sunscreen', 'Facial Kit', 'Lip Glow', 'Lip Balm', 'Hair Oil']
for item in products:
    print(item)

for ch in 'Nexperts Academy':
    print(ch,end=" ")

name=input('Enter Your name: \t')
print('Characters of your name as follows: \n')
for ch in name:
    print(ch)

num=int(input('Please enter number to find out table: \t'))
print(f'Table of Number {num} as follow \n')
for i in range(1,11):
    print(f'{num}*{i}=\t{num*i}')

for i in range (10):
    print(i)

for i in range (10):
    print(i,end="\t")

#A tuple is an immutable data type in python.
#One example of for loop to iterate through tuple

players=('MSD','VK','KL','RS')
for player in players:
    print(player)

players=('Lionel Messi','Cristiano Ronaldo','Pele','Diego')
for player in players:
    print(player,end=" ")
