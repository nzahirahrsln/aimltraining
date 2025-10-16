# import os

# print ('Current Directory: ',os.getcwd())


# functions = inspect.getmembers(os, inspect.isbuiltin)

# print('All Function in os module')
# for n, func in functions:
#     print(n)

#Create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folder_name=input('Enter Folder Name to create: \t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')    

#Rename a folder
#Exercise
#  os.rename(folder_name, "renamed_folder")
 # write code to rename a folder
# you will take folderName from user
# if it is exist , you will ask new name and rename it
import calc
print('Average of 10,20 is: \t',calc.avg(10,20))