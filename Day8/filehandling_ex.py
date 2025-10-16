import os 
file_path= r 'D:\AI_ML_Training\Python\Day8'
file=os
filename=input('Enter File Name to Create File: \t')
fullpath=os.path.join(filepath,filename)
file=open(fullpath, 'w')
content=input('Enter text to write in File: \t')
file.write(content)
print(f'File {filename} create at {fullpath} and content saved in file')
file.close 