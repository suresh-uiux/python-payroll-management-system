import json
import os

FILE = "employees.json"


class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        tax = 0.08 * self.basic_salary

        net_salary = self.basic_salary + hra + da - tax

        return {
            "basic": self.basic_salary,
            "hra": hra,
            "da": da,
            "tax": tax,
            "net": net_salary
        }


class PayrollSystem:

    def __init__(self):
        self.employees = self.load_data()

    def load_data(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(FILE, "w") as f:
            json.dump(self.employees, f, indent=4)

    # ---------- FEATURES ----------
    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            salary = float(input("Enter Basic Salary: "))

            emp = Employee(emp_id, name, salary)
            self.employees.append({
                "id": emp.emp_id,
                "name": emp.name,
                "salary": emp.basic_salary
            })

            self.save_data()
            print("✅ Employee Added Successfully")

        except ValueError:
            print("❌ Invalid salary input!")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return

        print("\n--- Employee Records ---")
        for e in self.employees:
            print(f"ID: {e['id']} | Name: {e['name']} | Salary: {e['salary']}")

    def generate_payslip(self):
        emp_id = input("Enter Employee ID: ")

        for e in self.employees:
            if e["id"] == emp_id:
                emp = Employee(e["id"], e["name"], e["salary"])
                salary = emp.calculate_salary()

                print("\n------ PAYSLIP ------")
                print("Employee ID:", emp.emp_id)
                print("Name:", emp.name)
                print("Basic Salary:", salary["basic"])
                print("HRA:", salary["hra"])
                print("DA:", salary["da"])
                print("Tax:", salary["tax"])
                print("Net Salary:", salary["net"])
                print("----------------------")
                return

        print("❌ Employee not found!")

    def monthly_summary(self):
        total_salary = 0

        for e in self.employees:
            emp = Employee(e["id"], e["name"], e["salary"])
            sal = emp.calculate_salary()
            total_salary += sal["net"]

        print("\n📊 Monthly Payroll Summary")
        print("Total Employees:", len(self.employees))
        print("Total Payout:", total_salary)


def menu():
    system = PayrollSystem()

    while True:
        print("\n===== PAYROLL SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Generate Payslip")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            system.add_employee()

        elif choice == "2":
            system.view_employees()

        elif choice == "3":
            system.generate_payslip()

        elif choice == "4":
            system.monthly_summary()

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice")


menu()
