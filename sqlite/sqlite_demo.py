import sqlite3
from employee import Employee
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# c.execute("INSERT INTO employees VALUES('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='schafer'")
# print(c.fetchall())


# conn.commit()

# c.execute("SELECT * FROM employees WHERE last=?", ('schafer', ))
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
# print(c.fetchall())

conn = sqlite3.connect(':memory:')

c = conn.cursor()

# Create the employees table
c.execute("""CREATE TABLE IF NOT EXISTS employees (
    first text,
    last text,
    pay integer
)""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", 
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emp_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees Set pay = :pay
                  Where first = :first and last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first and last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emp_by_name('Doe')
print(emps)

conn.close()