# def fun(a=10, b=20):
#     print(a, b)

# fun(20,30)
# fun(50)
# fun()

# def fun(a=2,b=3):
#     print(a+b)

# fun()

# fun = lambda a,b : a+b
# print(fun(10,20))
# gst = lambda: 18
# print(gst())

# adds = lambda *args : sum(args)
# print(adds(1029,9090))

# adds = lambda **kwargs : f'My name is {kwargs.get('name')}.'
# print(adds(name = 'Harshi'))

# fun = lambda a=2,b=2 : a+b
# print(fun(10,20))

# num1 = 5
# num2 = 6
# num3 = fun(num1,num2)
# print(num3)

# print((lambda a, b : a + b)(11,22))

# from functools import reduce
# dobs = [4, 17, 9, 22, 25, 31, 10]
# evens = list(filter(lambda d: d % 2 == 0, dobs))
# print(evens)
# double = list(map(lambda d: d * 2,evens))
# print(double)
# sum = reduce(lambda a, b: a + b, double)
# print(sum)

#OOPS
# entity - attributes and functionalities
# employee - id, name, salary, work(), leave()

class Employee :

    def __init__(self, id, name, salary, city):   #__init__ = dunder or magic methods
        self.id = id
        self.name = name
        self.__salary = salary #private_field
        self.city = city

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}, Salary:{self.__salary}, City:{self.city}'

class Manager (Employee) :
    def __init__(self, id, name, salary, city, department):
        super().__init__(id, name, salary, city)
        self.department = department

    def __str__(self):
        return super().__str__() + f', Department: {self.department}'
    
from functools import reduce

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employees(self):
        if not self.employees:
            print("No employees to display.")
        for employee in self.employees:
            print(employee.id , employee.name, employee.get_salary(), employee.city)

    def edit_employee(self, id, new_name=None, new_salary=None, new_city=None):
        employee = self.find_employee(id)
        if employee:
            if new_name:
                employee.name = new_name
            if new_salary:
                employee.set_salary(new_salary)
            if new_city:
                employee.city = new_city
            print(f"Employee {id} updated successfully.")
        else:
            print(f"Employee with ID {id} not found.")

    def delete_employee(self, id):
        employee = self.find_employee(id)
        if employee:
            self.employees.remove(employee)
            print(f"Employee {id} deleted successfully.")
        else:
            print(f"Employee with ID {id} not found.")

    def find_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None
    
    def display_names(self):
        list_upper = list(map(lambda emp : emp.name.upper(), self.employees))
        print(list_upper)

    def threshold_filter(self, threshold):
        filtered_list = filter(lambda emp: emp.get_salary() > int(threshold), self.employees)
        for emp in filtered_list:
            print(emp)
            
    def total_salary(self):
        if self.employees:
            total = reduce(lambda a, b: a.get_salary() + b.get_salary(), self.employees)
            print(total)
        else:
            print("No items in list")

    
def main_menu():
    ems = EmployeeManagementSystem()
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Edit Employee")
        print("4. Delete Employee")
        print("5. Add Manager")
        print("6. Exit")
        print("7. Print Names")
        print("8. Display employees with salary above value")
        print("9. Total Salary")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Employee Salary: "))
            city = input("Enter Employee City: ")
            emp = Employee(emp_id, name, salary, city)
            ems.add_employee(emp)

        elif choice == "2":
            ems.view_employees()

        elif choice == "3":
            emp_id = int(input("Enter Employee ID to Edit: "))
            print("Leave fields blank if no change is needed.")
            name = input("Enter New Name (optional): ")
            salary = input("Enter New Salary (optional): ")
            city = input("Enter New City (optional)")

            name = name if name else None
            salary = float(salary) if salary else None
            city = city if city else None
            ems.edit_employee(emp_id, name, salary, city)

        elif choice == "4":
            emp_id = int(input("Enter Employee ID to Delete: "))
            ems.delete_employee(emp_id)

        elif choice == "5":
            emp_id = int(input("Enter Manager ID: "))
            name = input("Enter Manager Name: ")
            salary = float(input("Enter Manager Salary: "))
            city = input("Enter Manager City: ")
            department = input("Enter Manager Department: ")
            manager = Manager(emp_id, name, salary, city, department)
            ems.add_employee(manager)

        elif choice == "6":
            print("Exiting Employee Management System")
            break

        elif choice == "7":
            ems.display_names()

        elif choice == "8":
            threshold = float(input("Enter threshold salary: "))
            ems.threshold_filter(threshold)

        elif choice == "9":
            ems.total_salary()

        else:
            print("Invalid choice. Please try again.")

main_menu()
    
# emp1 = Employee(98, 'Sonu', 89898, 'Pune')
# emp2 = Employee(97, 'Tonu', 9798, 'Goa')
# ems = EmployeeManagementSystem()
# ems.add_employee(emp1)
# ems.add_employee(emp2)
# manager1 = Manager(78, 'Monu', 978987, 'Jaipur', 'dev')
# ems.add_employee(manager1)
# ems.view_employees()
# ems.edit_employee(97,None,9000,None)
# ems.delete_employee(97)
# ems.view_employees()



# emp1 = Employee(101, 'Sonu', 10.25)
# print(str(emp1))

# print(emp1.id,emp1.name, emp1.get_salary())
# emp1.set_salary(12)
# print(emp1.id, emp1.name, emp1.get_salary())

# Inheritance 

# class ContractualEmployee (Employee): 
#     def show_bonus(self):
#         print(self.get_salary()+10)
#     # polymorphism
#     def emp_data(self):
#         print(self.id, self.name, self.get_salary())

# emp3 = ContractualEmployee(103, 'Ponu', 15.25)
# emp3.emp_data()
# emp3.show_bonus()

# class Class:
#     def __init__(self, id, salary, name): 
#         self.id = id
#         self._salary = salary
#         self.__name = name

# class ChildClass (Class):
#     pass

# cls = Class(1, 10, 'a')

# print(cls._Class__name) #possible but not recommended
# print(cls._salary) #possible but not recommended

# cls2 = ChildClass(2, 20, 'b')
# print(cls2._salary) #possible but not recommended


