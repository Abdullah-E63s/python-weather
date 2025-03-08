class Company:
    class Employee:
     def __init__(self, name, position):
        self.name = name
        self.position = position

     def get_details(self):
        return f"Name: {self.name}, Position: {self.position}"
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
       new_employee = self.Employee(name, position)
       self.employees.append(new_employee)
       
    
    def list_employees(self):
       return [ employee.get_details() for employee in self.employees]

company1 = Company("Krusty krabs")
company2 = Company("Chum Bucket")

company1.add_employee("Eugene", "Manager")
company1.add_employee("spongbob", "Cook")
company1.add_employee("squidward", "Cashier")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("karen", "Assistentant")




print(company2.company_name)
for employee in company2.list_employees():
    print(employee)