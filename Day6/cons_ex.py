class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def display(self):
        print('ID: ' ,self.id)
        print('Name:  ' ,self.name)
        print('Quali: ' ,self.qual)

class Dev(Emp):
    def __init__(self, id, name, qual, domain, project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print('Domain: ' ,self.domain)
        print('Project: ' ,self.project)

#create one Emp object with id=1, name='Sam', qual='MCA'
emp=Emp(1, 'Sam', 'MCA')
# create one Dev object with id=3, name='Ravi',qual ='MTech',Project='eShopping', Domain='dot net'
dev=Dev(3, 'Ravi', 'Mtech', 'e-Shopping', 'dotnet')
# Display dev details
print('Developer Details as follows')
dev.show_info()
#Display Emp details
print('Developer Details as follows')
dev.show_info()
# Display Emp details 
print('Employee Details as follows')
emp.show_info()