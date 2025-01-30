from functools import reduce

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    #getter functions
    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    #setter functions 
    def set_salary(self, salary):
        self._salary = salary

    def __str__(self):
        return f"Employee(Name: {self._name}, Salary: {self._salary})"

    def _add_(self, other):
        return self._salary + other._salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def get_department(self):
        return self._department

    def __str__(self):
        return f"Manager(Name: {self._name}, Salary: {self._salary}, Department: {self._department})"

class ManagementSystem:
    def __init__(self):
        self.employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def viewEmployees(self):
        for emp in self.employees:
            print(emp)

    def deleteEmployee(self, name):
        self.employees = [emp for emp in self.employees if emp.get_name() != name]

    def editEmployeeSalary(self, name, new_salary):
        for emp in self.employees:
            if emp.get_name() == name:
                emp.set_salary(new_salary)
                break

    def getTotalExpenditure(self):
        return reduce(lambda x, y: x + y, [emp.get_salary() for emp in self.employees])

    def getHigherSalaryEmployees(self, threshold):
        return list(filter(lambda emp: emp.get_salary() > threshold, self.employees))

    def getUppercaseNames(self):
        return list(map(lambda emp: emp.get_name().upper(), self.employees))


if __name__ == "__main__":
    system = ManagementSystem()
    emp1 = Employee("Aman", 40000)
    emp2 = Employee("Shubham", 70000)
    mngr1 = Manager("Divyansh", 80000, "5g")

    system.addEmployee(emp1)
    system.addEmployee(emp2)
    system.addEmployee(mngr1)

    print("All Employees list :")
    system.viewEmployees()

    print("\nEmployees having Higher Salary (>50000):")
    high_salary_emps = system.getHigherSalaryEmployees(50000)
    for emp in high_salary_emps:
        print(emp)

    print("\nTotal Salary Expenditure is :", system.getTotalExpenditure())

    print("\n Employee Names in Uppercase letter are :", system.getUppercaseNames())

     