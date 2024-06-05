class Company:
    def __init__(self, name, industry, founding_year):
        self.name = name
        self.industry = industry
        self.founding_year = founding_year
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                return f"Employee with ID {employee_id} has been removed."
        return f"No employee with ID {employee_id} found."

    def list_employees(self):
        employee_list = "\n".join([f"{employee.name} - {employee.employee_id} - {employee.salary} - {employee.experience} years experience"
                                   for employee in self.employees])
        return f"Employees of {self.name}:\n{employee_list}"


class Employee:
    def __init__(self, name, employee_id, department, salary, experience):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.experience = experience

    def __repr__(self):
        return f"{self.name} - {self.employee_id} - {self.salary} - {self.experience} years experience"


# Example usage
company = Company("Tech Solutions", "Information Technology", 1990)

employee1 = Employee("John Doe", 1001, "Engineering", 60000, 5)
employee2 = Employee("Jane Smith", 1002, "HR", 55000, 3)
employee3 = Employee("Bob Johnson", 1003, "Marketing", 62000, 7)

company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

print(company.list_employees())

company.remove_employee(1002)
print(company.list_employees())
