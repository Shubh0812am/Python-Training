
#Encapsulation 
class Employee:
    #special method == constructor 
    def __init__(self,id,name,salary):
        self.id = id
        self.name =  name 
        self.__salary = salary #private field

    def emp_data(self):
        print(self.id, self.name) 

    def set_salary(self,salary):
        self.__salary = salary 

    def get_salary(self):
        return self.__salary

#emp1 = Employee(101,'Sonu') 
#print(emp1.id, emp1.name)
#emp1.emp_data()

emp2 = Employee(101,'Monu',10.25) 
emp2.set_salary(12.50) 
print(emp2.id,emp2.name,emp2.get_salary())

