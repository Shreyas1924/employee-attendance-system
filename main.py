# Employee Attendance Management System
# -------------------------------------
# This is a simple Python CLI project to manage employee attendance.
# Features:
# - Add employee
# - View employees
# - Search employee
# - Update attendance
# - Delete employee
# - Attendance report
#
# Data is stored in a text file (attendance.txt).
# Author: Shreyas S D


FILE_NAME = "attendance.txt"


# ---------- CHECK UNIQUE ID ----------
def is_unique_id(emp_id):
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                existing_id = int(line.split(",")[0])
                if existing_id == emp_id:
                    return False
    except FileNotFoundError:
        return True
    return True


# ---------- ADD EMPLOYEE ----------
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    if not is_unique_id(emp_id):
        print("Error: Employee ID already exists!")
        return

    name = input("Enter Employee Name: ").strip()
    if name == "":
        print("Employee name cannot be empty.")
        return

    try:
        days = int(input("Enter Days Present: "))
    except ValueError:
        print("Days Present must be a number.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{days}\n")

    print("Employee added successfully.")


# ---------- VIEW EMPLOYEES ----------
def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nID   Name   Days")
            print("------------------")
            for line in file:
                if line.strip() == "":
                    continue
                emp_id, name, days = line.strip().split(",")
                print(f"{emp_id}   {name}   {days}")
    except FileNotFoundError:
        print("No employee records found.")


# ---------- SEARCH EMPLOYEE ----------
def search_employee():
    try:
        search_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                emp_id, name, days = line.strip().split(",")
                if int(emp_id) == search_id:
                    print(f"Found → ID: {emp_id}, Name: {name}, Days: {days}")
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("No records found.")


# ---------- UPDATE ATTENDANCE ----------
def update_attendance():
    try:
        update_id = int(input("Enter Employee ID to update: "))
        new_days = int(input("Enter new Days Present: "))
    except ValueError:
        print("ID and Days Present must be numbers.")
        return

    updated = False
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in records:
                if line.strip() == "":
                    continue
                emp_id, name, days = line.strip().split(",")
                if int(emp_id) == update_id:
                    file.write(f"{emp_id},{name},{new_days}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Attendance updated successfully.")
        else:
            print("Employee ID not found.")

    except FileNotFoundError:
        print("No records found.")


# ---------- DELETE EMPLOYEE ----------
def delete_employee():
    try:
        delete_id = int(input("Enter Employee ID to delete: "))
    except ValueError:
        print("Employee ID must be a number.")
        return

    found = False
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in records:
                if line.strip() == "":
                    continue
                emp_id, name, days = line.strip().split(",")
                if int(emp_id) == delete_id:
                    found = True
                    continue
                file.write(line)

        if found:
            print("Employee deleted successfully.")
        else:
            print("Employee ID not found.")

    except FileNotFoundError:
        print("No records found.")


# ---------- ATTENDANCE REPORT ----------
def attendance_report():
    TOTAL_DAYS = 30
    try:
        with open(FILE_NAME, "r") as file:
            print("\nID   Name   Days   %   Status")
            print("--------------------------------")
            for line in file:
                if line.strip() == "":
                    continue
                emp_id, name, days = line.strip().split(",")
                days = int(days)
                percent = (days / TOTAL_DAYS) * 100

                if percent >= 75:
                    status = "Regular"
                elif percent >= 50:
                    status = "Warning"
                else:
                    status = "Defaulter"

                print(f"{emp_id}   {name}   {days}   {percent:.1f}%   {status}")

    except FileNotFoundError:
        print("No records found.")


# ---------- MAIN MENU ----------
while True:
    print("\n--- Employee Attendance System ---")
    print("1. Add Employee")
    print("2. Update Attendance")
    print("3. View All Employees")
    print("4. Search Employee by ID")
    print("5. Attendance Report")
    print("6. Delete Employee")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        update_attendance()
    elif choice == "3":
        view_employees()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        attendance_report()
    elif choice == "6":
        delete_employee()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
