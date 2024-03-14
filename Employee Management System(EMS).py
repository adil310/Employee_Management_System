
# Employee Management System (EMS) Application

# Function to add a new employee to the file

def add_employee():
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name:")
    position = input("Enter Employee Postion:")
    salary = input("Enter Employee Salary:")

    with open("employees.txt", "a") as file:
        file.write(f"{employee_id}{name}{position}{salary}/n")
        print("Employee added successfully!/n")

    # Function to display employee details

        def display_employee_details():
         try:
             with open("employees.txt", "r") as file:
                 print("\nEmployee Details:")
                 print("ID\tName\tPosition\tSalary")
                 for line in file:
                     employee_data = line.strip().split(",")
                     print(f"{employee_data[0]}\t{employee_data[1]}\t{employee_data[2]}\t\t{employee_data[3]}")
                 print()
         except FileNotFoundError:
             print("No employee data found!\n")

             def main():
                 while True:
                     print("Employee Management System (EMS)")
                     print("1. Add a new employee")
                     print("2. Display employee details")
                     print("3. Exit")
                     choice = input("Enter your choice: ")

                     if choice == "1":
                         add_employee()
                     elif choice == "2":
                         display_employee_details()
                     elif choice == "3":
                         print("Exiting program. Goodbye!")
                         break
                     else:
                         print("Invalid choice! Please enter a valid option.\n")

             if __name__ == "__main__":
                 main()




