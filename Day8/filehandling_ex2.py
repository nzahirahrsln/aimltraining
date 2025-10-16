import os
filepath = os.getcwd()
filename = input('Enter File Name to update File: \t')
fullpath = os.path.join(filepath,filename)

if(os.path.exists(fullpath)):
    file = open(fullpath,'a')
    content=input('Enter tezt to add in file')
    file.write(content)
    print(f'File {filename} updated')
    file.close
else:
    print(f'No such file {filename} exist')