print("Hello! We are going to learn Tuple here")

subjects=('python', 'java', 'dotnet', 'sql', 'powerbi')
print('\n All Subject are: \n')
for sub in subjects:
    print(sub,end="\t")

numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
for num in numbers:
    print(num,end="\t")

#tupleName.index(item) will return the index of first occurrence of item in tupleName
search_num=int(input('\nEnter Number to find out index'))
if search_num in numbers:
    print(f'Index of {search_num} is: \t ',numbers.index(search_num))
else:
    print(f'No Such Number {search_num} in our tuple')


#tupleName.count(item): tupleName count(item) will return number of times item occurs in tupleName.
numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
print('All Numbers in tuple:',len(numbers))
for num in numbers:
    print(num,end="\t")
search_num=int(input('\nEnter Number to find out frequency:\t'))
if search_num in numbers:
    print(f'Number: {search_num} occurs : {numbers.count(search_num)} times')
else:
    print(f'No Such Number {search_num} in our tuple')


#tupleName.count(item): tupleName count(item) will return number of times item occurs in tupleName.
numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
print('All Numbers in tuple:',len(numbers))
for num in numbers:
    print(num,end="\t")
search_num=int(input('\nEnter Number to find out frequency:\t'))
if search_num in numbers:
    print(f'Number: {search_num} occurs : {numbers.count(search_num)} times')
else:
    print(f'No Such Number {search_num} in our tuple')