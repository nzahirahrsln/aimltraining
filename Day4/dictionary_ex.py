employee={"id":1,
          "name":"Sam",
          "salary":55000.50
          }

print("Employees Details as follows: ")
for key, value in employee.items():
    print(key,"->", value)

# Adding key in dictionary
employee["city"]="Muscat"
print('\nDictionary after adding City\n')

for key, value in employee.items():
    print(key,"->", value)

del employee["salary"]
print("\n Employee Details after deleting Salary \n")
for key, value in employee.items():
    print(key, "->", value)


employee={"id":1,
          "name":"Sam",
          "salary":55000.50
          }

print('All keys from Employee')
for k in employee.keys():
    print(k, end="\t")

print('\n All values from Employee \n')
for v in employee.values():
    print(v, end="\t")

print('\nKey:Value')
for k,v in employee.items():
    print(k," :",v)

print('\n Dictionary as follows')
print(employee)
del employee["salary"]
print('After deleting salary')
for k,v in employee.items():
    print(k," :" ,v)


