def input_num(num): # function for taking a input
      while True:
        try:
            return float(input(num))
        except ValueError:
            print("invalid please enter a number only!!!")


def ZeroDvision_error(): # function for handling zero divison error by (try, except)
    while True:
      try:
         b = input_num("enter a non zero 2nd number for division  : ")
         if b !=0:
            return b 
         break
      except ZeroDivisionError():
         print("cannot divide by zero")
    
print("enter 2 numbers to see thier division") # displaying to the user
   
a = input_num("\nenter the first number for division : ") #taking inputs
b = input_num("enter the 2nd number for division  : ")

if b !=0: #if b is not 0
 print(f"{a} / {b} = {a/b}")

elif b == 0: # if b is zero
  b = ZeroDvision_error() #calling the function to handle
  print(f"{a} / {b} = {a/b}") # after handling 

