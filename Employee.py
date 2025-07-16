
class Employee:
    def __init__(self, id, salary, name, age):
        self.__id = id
        self.name = name
        self.age = age
        self.__salary = salary
        
    def get_id(self):
        return self.__id
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary
    
    def display(self):
        print(f'''
              Employee Details:
              Name : {self.name}
              Age : {self.age}
              Employee ID : {self.__id}
              Salary : {self.__salary}
              ''')

class Manager(Employee):
    def __init__(self, id, salary, name, age, dept):
        super().__init__(id, salary, name, age)
        self.dept = dept
        
    def display(self):
        super().display()
        print(f"Department : {self.dept}")

class Developer(Employee):
    def __init__(self, id, salary, name, age, programming_lan):
        super().__init__(id, salary, name, age)
        self.programming_lan = programming_lan
        
    def display(self):
        super().display()
        print(f"Programming Language : {self.programming_lan}")

employees = []

print("--- Python OOP Project: Employee Management System ---")

while True:
    
    print('''
        Choose an operation:
        1. Create a Person
        2. Create an Employee
        3. Create a Manager
        4. Show details
        5. Compare salaries
        6. Exit
        ''')

    select = int(input("Enter Your Choice: "))
    
    match select:
        case 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            print(f"Person created with Name: {name} and Age: {age}")
            
        case 2:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            eid = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            programming_lan = input("Enter Programming Language: ")
            emp = Developer(eid, salary, name, age, programming_lan)
            employees.append(emp)
            print("Employee created successfully!")
            
        case 3:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            eid = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            mgr = Manager(eid, salary, name, age, dept)
            employees.append(mgr)
            print("Manager created successfully!")
            
        case 4:
            if not employees:
                print("No employees to display!")
            else:
                for emp in employees:
                    emp.display()
                    
        case 5:
            if len(employees) < 2:
                print("Need at least 2 employees to compare salaries!")
            else:
                emp1 = employees[0]
                emp2 = employees[1]
                if emp1.get_salary() > emp2.get_salary():
                    print(f"{emp1.name} has higher salary than {emp2.name}")
                elif emp1.get_salary() < emp2.get_salary():
                    print(f"{emp2.name} has higher salary than {emp1.name}")
                else:
                    print("Both employees have the same salary")
                    
        case 6:
            print("Exit...!!! BYE BYE...")
            break
            
        case _:
            print("Invalid choice! Please try again.")