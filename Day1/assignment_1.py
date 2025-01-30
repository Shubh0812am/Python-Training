employees = [] 

#create 4 function 

def addEmployee():
    emp_id = int(input("Enter emp id: ")) 
    name = input("Enter emp name: ")
    salary = int(input("Enter emp salary: "))
    city = input("Enter City: ")
    employee = {"emp_id":emp_id , "name":name,"salary":salary,"city":city} 
    employees.append(employee)
    print("New Employee has been added!!")

def viewEmployee():
    #what if no employees 
    if not employees:
        print("Currently No Employees!!") 
        return
    for emp in employees:
        print(f"ID: {emp['emp_id']} , Name: {emp['name']} , Salary: {emp['salary']} , City: {emp['city']}")

def searchEmployee():
    parameter = input("Searching by Name or City?").strip().lower()
    if parameter == "name":
        name = input("Enter the name which needs to be searched: ")
        res = [emp for emp in employees if emp['name'].lower() == name.lower()] 
    elif parameter == "city":
        city = input("Enter the city which needs to be searched: ")
        res = [emp for emp in employees if emp['city'].lower() == city.lower()] 
    else:
        print("Invalid search!!") 
        return
    #printing the search results
    if res:
        print("\n Search res is: ")
        for emp in res:
            print(f"ID: {emp['emp_id']} , Name: {emp['name']} , Salary: {emp['salary']} , City: {emp['city']}")
    else:
        print("Employee not exists!!")
         

def editEmployee():
    emp_id = int(input("Enter emp_id: ")) 
    for emp in employees:
        if emp['emp_id'] == emp_id:
            print("1. Edit Employee Name")
            print("2. Edit Employee Salary")
            print("3. Edit Employee City")
            choice= int(input("Enter Choice: ")) 
            if choice == 1: 
                emp['name']=input("Enter new name for employee: ")
            elif choice ==2:
                emp['salary']=int(input("Enter new salary for employee: "))
            elif choice ==3: 
                emp['city']=input("Enter new city for employee: ")
            else:
                print("Invalid choice!!")
                return
            print("Details of Employee has been Edited!!")
            return
    #what if invalid emp_id
    print("Employee not exists!!")
    

def deleteEmployee():
    emp_id=int(input("Enter which emp_id needs to be deleted: ")) 
    for emp in employees:
        if emp['emp_id'] == emp_id:
            employees.remove(emp)
            print("employee deleted!!")#after emp has been deleted successfully
            return
    #what if given emp_id not valid 
    print("Invalid emp_id!!")

def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Edit Employee")
        print("5. Delete Employee")
        print("6. Exit Employee")
        choice = int(input("Enter your choice: ")) 
        if choice == 1: 
            addEmployee()
        elif choice == 2:
            viewEmployee()
        elif choice == 3:
            searchEmployee()
        elif choice == 4:
            editEmployee()
        elif choice == 5:
            deleteEmployee()
        elif choice == 6:
            break
        else:
            print("Invalid choice!!")


menu()
