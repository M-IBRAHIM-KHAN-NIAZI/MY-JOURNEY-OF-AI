class employee():
    salary=12000
    increment=20
    @property
    def salaryafterincrement(self):
        return(self.salary +self.salary *(self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary / self.salary)-1)*100


a=employee()
# print(a.salaryafterincrement)
salaryafterincrement=300
print(a.increment)