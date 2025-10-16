print("List Example One")

#my_list = [10, 20, 30, "Python", None, True, 12.45]

my_list = [10, 20, 30, "Python",None,True,12.45,'Ravi']
print('Number of items in list are:',len(my_list))

for item in my_list:
    print(item)


print("Second Example of List")
employees=["Sam", "Ali", "Amir", "Khays", "Chong", "Ravi", "Mina", "Mila"]
print("Number of Employees", len(employees))
print('All Employees')
# for name in employees:
#     print(name)
for name in employees:
    print(employees,end=" ")

# Sort Example
#listName.sort()
employees.sort()
print("\n List after sorting")
for e in employees:
    print(e, end=" ")

# Reverse example
#listName.reverse()
employees.reverse()
print('\n Employees in Descending Order')
for e in employees:
    print(e, end=" ")

# append,remove,pop insert method
employees=["Ali", "Abu", "Khays", "Hafiz", "Ira", "Apek", "Zack", "Sophea"]
print("Number of employees" ,len(employees))
for name in employees:
    print(employees,end="")


#append : adds the item at the end of list
newEmp=input("\nEnter employee name to add in list:\t")
employees.append(newEmp)
print('\nAfter adding New Employee: Number of employees are:',len(employees))
for name in employees:
    print(name,end=" ")


#insert(index,item): This will add item at  given index
newEmp=input("\nEnter employee name to add in list:\t")
pos=int(input("Enter poistion where you want to insert inside list:\t"))
employees.insert(pos,newEmp)
print('\nAfter adding New Employee: Number of employees are:',len(employees))
for name in employees:
    print(name,end=" ")


# append,remove,pop insert method
employees=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
print("Number of Employees",len(employees))
for name in employees:
    print(name,end=" ")

#listName.remove(item): Will remove item from the list
delEmp=input('Employee to remove from the list:\t')
if delEmp in employees:
    employees.remove(delEmp)
    print(f"Number of Employees after deleting {delEmp} in list are: ",len(employees))
for name in employees:
    print(name, end=" ")
else:
    print(f'No such item {delEmp} in employee list')


#pop example
employees=["Ali", "Abu", "Khays", "Hafiz", "Ira", "Apek", "Zack", "Sophea"]
print("Number of employees" ,len(employees))
for name in employees:
    print(employees,end="")

#listName.pop(index): Will delete element at given index & return its value
del_index=int(input('Enter index to pop item: \t'))
print('Pop Result: ' ,employees.pop(del_index))

print("Number of employees after pop() are: " ,len(employees))
for name in employees:
    print(employees,end=" ")

#find out first and last element from the list
employees=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
print("Number of Employees",len(employees))
for name in employees:
    print(name,end=" ")
count=len(employees)
print('\n First Element of employees list is: ',employees[0])
print('\n Last Element of employees list is: ',employees[-1])
print('\n second Last Element of employees list is: ',employees[-2])
print('\n Last Element of employees list is: ',employees[count-1])
