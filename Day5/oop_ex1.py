# class Emp:
#     def display(self):
#         print('Display of Employee Class')


# obj = Emp()
# obj.display()       

#class className:
    #body of class 
    #attribute Method ,constructors

#objectName=ClassName()
# objectName.MethodName()    

# e=Emp()
# e.display()

#Second Example
class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print('Employee Id:',self.eid)
        print('Employee Name:',self.ename)

e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.reg(1,'Sam')
e2.reg(102,'Neha')
e3.reg(103,'Jai')
print('First Employee Details')
e1.display() 
print('Second Employee Details')
e2.display()
print('Third Employee Details')
e3.display()