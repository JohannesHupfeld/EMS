import csv
import os

class Employee:
      
  def __init__(self, _first_name, _last_name, _department, _date_of_emplpoyment, _salary, _id):
      self.first_name = _first_name
      self.last_name = _last_name
      self.department = _department
      self.date_of_employment = _date_of_emplpoyment
      self.salary = _salary
      self.id = _id
      
def menu():
  print("Welcome to Employee Management Record")
  print("Press ")
  print("1 to Add Employee")
  print("2 to Remove Employee ")
  print("3 to Promote Employee")
  print("4 to Display Employees")
  print("5 to Exit")
  
  # Taking choice from user
  ch = int(input("Enter your Choice "))
  if ch == 1:
      create_employee()
      
  elif ch == 2:
      Remove_Employee()
      
  elif ch == 3:
      Update_Employee()
      
  elif ch == 4:
      get_employee()
      
  elif ch == 5:
      exit(0)
      
  else:
      print("Invalid Choice")
      menu()
      
def get_employee(self):
    try:
      with open('./resources/employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
          print(row)
    except FileNotFoundError: print("File Not Found")

def create_employee(self):
    employee_list = []

    employeeCounter = int(input("How many employees do you want to add? (int) \n"))
    counter = 1
    while counter <= employeeCounter:
      employee = {}
      while True:
        try:
          first_name = input("Enter your first name: \n")
          last_name = input("Enter your last name: \n")
          department = input("Enter your department: \n")
          date_of_employment = complex(input("Enter your date of employment: \n"))
          salary = int(input("Enter your salary: \n"))


          employee["id"] = counter
          employee["First Name"] = first_name
          employee["Last Name"] = last_name
          employee["Department"] = department
          employee["Date of Employment"] = date_of_employment
          employee["Salary"] = salary

          employee_list.append(employee)
        except ValueError:
          print("Salary must be an integer")
        else: 
          break

      counter += 1
    print(employee_list)
    
    try:
      with open("./resources/employees.csv", "wt") as file:
        writer = writer(file, header)
        header = ["first name", "last name", "department", "date_of_employment", "salary", "id"]

        writer.writerows(employee_list)         
    except FileNotFoundError: print("File Not Found")

# def update_employee():
  
# def delete_employee():      
  
  