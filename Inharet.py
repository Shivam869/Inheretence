class person(object):
    def __init__(self,name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self, name, idnumber)
a=employee('Shivam',2382010,"$1500000","COO")
a.display()