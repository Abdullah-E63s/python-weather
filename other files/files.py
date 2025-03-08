import os # to find the path directory


def input_file_name():
    while True:
        f = input("Tell your file name: ")
        if f: 
            if not os.path.exists(f):
                open(f, "x").close()  # Creates the file if it doesn't exist
                return f
            else:
                print("\nThe file already exists, please enter a new file name.")
        else:
            print("\nFile name cannot be empty. Please enter a valid file name.")

def contents(f):
    with open(f, "a") as file:  # Open files
        while True:
            content = input("\n Write what you want to save in the file (type 'done' when finished): ")
            if content.lower() == 'done':
                break
            file.write(content + "\n")  # Writes content to the file

def read_file(f):
    with open(f, "r") as file:  # Open file in read mode just to see in the terminal
        print(file.read())

file_name = input_file_name()  
contents(file_name)  
read_file(file_name)  # file is already created and the contents are saved this is just for showing it in the termianl

while True:
    yn = input("\nDo you want to create another file? Type 'yes' or 'no': ").lower() #.lower to check the end charachter or string
    
    if yn == 'yes':
        file_name = input_file_name()  # Create a new file if user says 'yes'
        contents(file_name)
        read_file(file_name)
        print("\nYour new file is ready.")
    elif yn == 'no':
        print("\nYour files are ready.")
        break
    else:
        print("Invalid command. Please enter only 'yes' or 'no'.")
        