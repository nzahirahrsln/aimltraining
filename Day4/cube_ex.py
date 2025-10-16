def cube(num):
    return num*num*num
given_num=int(input('Enter Number to find out cube of number:\t'))
print(f'Number is: {given_num} cube is',cube(given_num))

#Write a function to calculate  bonus of given salary
#function take salary as input and return bonus 10% of salary.
def calc_bonus(salary):
    return salary*0.10

salary=float(input('Enter Salary to find out bonus:\t'))
print(f'Salary is: {salary} bonus is:\t',calc_bonus(salary))