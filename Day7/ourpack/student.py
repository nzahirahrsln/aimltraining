class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def displayInfo(self):
        print('Student Id: ' ,self.id)
        print('Student Name: ' ,self.name)