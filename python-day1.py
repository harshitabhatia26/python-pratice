#a,b,c=10,5,8
#if a>b and b<c:
#    print('yes')
#else:
#    print('no')

#a,b = 5,5
#if a>b:
#    print(a>b)
#elif a<b:
#    print(a<b)
#else:
#    print('other')

# count = 1
# while count <= 5:
#     print(count)
#     count+=1

# employees = ['Sonu','Monu','Tonu','Sona']

# for i in employees:
#     print(i)

# for i in range (1,5):
#     print(i)

# emp_details = {'eid': 101, 'name': 'Sonu', 'salary': 10.25}

# for key, value in emp_details.items():
#     if(key=='salary'):
#         continue
#     print(key,value)

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

# a = input()
# num = int(a) % 8
# if num == 1 or num == 4:
#     print('lower')
# elif num == 2 or num == 5:
#     print('middle')
# elif num == 3 or num == 6:
#     print('upper')
# elif num == 7:
#     print('side lower')
# else:
#     print('side upper')


first_name = 'Harshita Bhatia'
# print(first_name[-1])

# print(first_name[2:4])
# print(first_name[0:9:3])
# print(first_name[::-1])

# print(first_name.swapcase())
# print(first_name * 3)

# text = '    abcdefghij  '
# # print(text.find('p'))
# # print(text.strip())

# employees = 'Sonu, Monu, Tonu'
# names = employees.split(', ')
# print(names)

# name = 'Sonu'
# salary = 1000

# print(f'My name is {name} and my salary is {salary}')

# data structures : list, dictionary, set, tuple
# my_dict = {'eid': 101, 'name':'Sonu', 'salary': 10.25}
# print(my_dict)
# my_dict['salary'] = 12.50
# print(my_dict)
# my_dict['city'] = 'Pune'
# print(my_dict)

# from collections import OrderedDict

# ord_dict = OrderedDict()
# ord_dict['Sonu'] = 10
# ord_dict['Monu'] = 20
# ord_dict['Tonu'] = 30
# print(ord_dict)

# for k,v in ord_dict.items():
#     print(k,v)

# from collections import Counter

# chars = Counter('aabbccsh')
# print(chars)

# my_list = ['abc','def','ghi','jkl','def','ghi','jkl','jkl']
# count = Counter(my_list)
# print(count)

# from collections import ChainMap

# my_list1 = {'Sonu': 10.25, 'Monu': 12.50}
# my_list2 = {'Tonu': 15.50, 'Sonu': 11.50}

# dicts = ChainMap(my_list1,my_list2)
# print(dicts)
# print(dicts['Tonu'])

# from collections import namedtuple

# Emp = namedtuple('Emp', ['eid','name','salary'])
# emp1 = Emp(101, 'Sonu', 10.25)
# emp2 = Emp(102, 'Monu', 12.25)
# print(emp1.name, emp1.salary)

# def fun():
#     print('fun function')

# fun()

# def add_nums(i,j):
#     return i+j

# sum = add_nums(10,20)
# print(sum)

# def add_nums(*nums):
#     print(sum(nums))

# add_nums(10,20)
# add_nums(10,20,30,40)

list_of_employees = [{'employee_id': 100, 'name': 'harshi', 'salary': 100, 'city': 'kota'}]
print('1. Add Employee')
print('2. View All Employees')
print('3. Edit Employee')
print('4. Delete Employee')
print('5. Search Employee')
print('6. Exit')

def add_employee(employee_id,name,salary,city):
    list = {'employee_id':employee_id,'name':name, 'salary':salary, 'city': city}
    list_of_employees.append(list)

def view_all():
    print(list_of_employees)

def edit_employee(employee_id):
    for employee in list_of_employees:
        if employee['employee_id'] == employee_id:
            print("Current data: ", employee)
            name = input("Enter new name (leave blank to keep current): ")
            salary = input("Enter new salary (leave blank to keep current): ")
            city = input("Enter new city (leave blank to keep current): ")

            if name:
                employee['name'] = name
            if salary:
                employee['salary'] = salary
            if city:
                employee['city'] = city

            print("Employee updated successfully")
            break
    else:
        print("Employee with ID", employee_id, "not found.")

def delete_employee(id_name_choice,delete_word):
    choice = id_name_choice
    if choice == '1':
        for employee in list_of_employees:
            if employee['employee_id'] == delete_word:
                list_of_employees.remove(employee)
    if choice == '2':
        for employee in list_of_employees:
            if employee['name'] == delete_word:
                list_of_employees.remove(employee)

    print('Employee deleted successfully')

def search_employee(city_name_choice,search_word):
    choice = city_name_choice
    if choice == '1':
        for employee in list_of_employees:
            if employee['name'] == search_word:
                print(employee)
    elif choice == '2':
        for employee in list_of_employees:
            if employee['city'] == search_word:
                print(employee)
    else: 
        print('Wrong choice input')
    
def employee_system():
        while True:
            choice =input()
            if choice == '1':
                employee_id = input('Enter employee id:')
                name = input('Enter employee name:')
                salary = input('Enter employee salary:')
                city = input('Enter employee city:')
                add_employee(employee_id, name, salary, city)
            elif choice == '2':
                view_all()
            elif choice == '3':
                employee_id = input('Enter employee id:')
                edit_employee(employee_id)
            elif choice == '4':
                id_name_choice = input('Choose 1 for id and 2 for name')
                delete_word = input('Enter word to delete')
                delete_employee(id_name_choice,delete_word)
            elif choice == '5':
                city_name_choice = input('Choose 1 for name and 2 for city')
                search_word = input('Enter word to search')
                search_employee(city_name_choice,search_word)
            elif choice == '6':
                break
            else:
                print('Invalid choice')

employee_system()
