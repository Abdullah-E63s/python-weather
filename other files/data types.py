import math

print("this program will show the desired calculations listed below")

print("""+ is for sum
- is for substraction
* is for Multiplication
/ is for divide
% is for Percentage
sqrt or Sqrt is for Square root
mod or Mod is for displaying the remainder""")

print("please only enter the symbols as written!!!")

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("invalid please enter a number only!!!")

def taking_operator():
    while True:
           op = input("enter the operation You want to perform from the above line : ")
           if op in ['+', '-', '*', '/', '%', 'Sqrt', 'sqrt', 'mod', 'Mod']:
                 return op
           print("invalid operation only enter these operations only!!! (+,-,*,/,%,mod,sqrt)")

a = input_number("enter any 1st number only numbers! : ")

b = input_number("enter any 2nd number only numbers! : ")

op = taking_operator()

if (op == '+'):
    print (f"the result of {a} + {b} = {a + b }")

elif (op == '-'):
     print (f"the result of {a} - {b} = {a - b }")

elif (op == '*'):
     print (f"the result of {a} * {b} = {a * b }")

elif (op == '/'):
        if (b == 0):
         print("Second number cannot be zero for division.")
        b = input_number("Please enter a non-zero second number: ")
        print(f"The result of {a} / {b} = {a / b}")

elif (op == 'sqrt' or op == 'Sqrt'):
    print(f"the sqaure root of {a} is {math.sqrt(a)} and the square root of {b} is {math.sqrt(b)}")

elif(op == 'mod' or op == 'Mod'):
    print (f"the result of {a} mod {b} = {a % b }")

elif (op == '%'):
    print(f"the percentage of {a}  is {a/100}% and the percentage of {b} is {b/100}%")
    print(f"the perecentage of both is {(a/b)*100}%")
