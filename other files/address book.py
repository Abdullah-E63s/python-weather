import os
import re
import pandas as pd

def input_file_name():
    while True:
        f = input("Enter your file name: ").strip()
        if f:
            # Block path traversal
            if any(char in f for char in {'/', '\\', '..'}):
                print("Invalid filename! Avoid slashes or '..'.")
                continue
            if not f.endswith(".csv"):
                f += ".csv"
            return f
        else:
            print("File name cannot be empty!")

def input_phone(prompt):
    phone_pattern = r'^\+?[\d\s\-\(\)]{7,}$'  # international format
    while True:
        phone = input(prompt).strip()
        if re.match(phone_pattern, phone):
            return phone
        print("Invalid phone number! Examples: +1 (555) 123-4567, 025551234")
def input_name(prompt):
    name_pattern = r'^[a-zA-Z\s\-\'À-ÿ]+$'  # Allows international characters and apostrophes
    while True:
        name = input(prompt).strip()
        if re.match(name_pattern, name, re.UNICODE):
            return name.title()  # Standardize capitalization
        print("Invalid name! Only letters, spaces, hyphens, and apostrophes allowed.")

def input_email(prompt):
    email_pattern = r'^[a-zA-Z_][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Cannot start with number
    while True:
        email = input(prompt)
        if re.match(email_pattern, email) or email == "":
            return email
        else:
            print("Invalid email format! Email cannot start with number. Example: name@domain.com")


def input_website(prompt):
    url_pattern = r'^(https?://)?[\w\-]+(\.[\w\-]+)+(:\d+)?(/\S*)?$'
    while True:
        url = input(prompt).strip()
        if not url or re.match(url_pattern, url, re.IGNORECASE):
            return url
        print("Invalid URL! Examples: http://example.com, www.site.org:8080/path")

def confirm_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in {'y', 'yes', 'n', 'no', 'Y', 'Yes'}:
            return response
        else:
         print("Please answer yes/no (y/n).")

address_book = {}

def get_input(prompt, default=""):  # Default to empty string
    user_input = input(prompt).strip()
    return user_input if user_input else default

# Function to add a contact
def add_contact(name, phone, email, job, address, website):
    if name in address_book:
        print(f"{name} already exists. Please choose another name.")
        return
    address_book[name] = {
        'Phone': phone,
        'Email': email,
        'Job': job,
        'Address': address,
        'Website': website
    }
    print(f"{name} added to address book.")

# Function to edit a contact
def edit_contact():
    if not address_book:
        print("Address book is empty.")
        return

    # Get valid contact name
    while True:
        name = input("Enter contact name to edit: ").strip()
        if name in address_book:
            break
        print(f"'{name}' not found. Try again.")

    updated = False

    print("\nWhich fields would you like to edit?")
    print("1. Phone")
    print("2. Email")
    print("3. Job")
    print("4. Address")
    print("5. Website")
    choices = input("Enter field numbers/names (e.g., 1 3): ").split()

    for original_choice in choices:
        current_choice = original_choice.strip().lower()
        while True:  # Retry loop for invalid choices
            valid_choice = False

            # Process the current choice
            if current_choice in {'1', 'phone'}:
                phone = input_phone("New phone number: ")
                address_book[name]['Phone'] = phone
                valid_choice = True
            elif current_choice in {'2', 'email'}:
                email = input_email("New email: ")
                address_book[name]['Email'] = email
                valid_choice = True
            elif current_choice in {'3', 'job'}:
                address_book[name]['Job'] = input("New job title: ")
                valid_choice = True
            elif current_choice in {'4', 'address'}:
                address_book[name]['Address'] = input("New address: ")
                valid_choice = True
            elif current_choice in {'5', 'website'}:
                website = input_website("New website: ")
                address_book[name]['Website'] = website
                valid_choice = True
            else:
                print(f"Invalid choice: '{current_choice}'")
                action = input("Skip or Retry? [s/r]: ").lower()
                if action == 'r':
                    current_choice = input("Re-enter field (e.g., 1): ").strip().lower()
                    continue  # Retry with new choice
                else:
                    print("Skipping invalid choice.")
                    break  # Move to next original choice

            # Exit retry loop if valid or skipped
            break

        if valid_choice:
            updated = True  # Track successful edits

    # Final update message
    if updated:
        print(f"\n✅ {name}'s details updated.")
    else:
        print("⚠️ No changes made.")

    print("Returning to main menu...")

# Function to view all contacts
def view_contacts():
    if address_book:
        print("Address Book Contacts:")
        for name, details in address_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print(f"Job: {details['Job']}")
            print(f"Website: {details['Website']}\n")
    else:
        print("Address book is empty.")

# Function to delete a contact
def delete_contact():
    if not address_book:
        print("Address book is empty. Redirecting to main menu...")
        return  # Redirect to main menu

    name = input("Enter the name of the contact to delete: ")
    if name in address_book:
        del address_book[name]
        print(f"{name} has been deleted from the address book.")
    else:
        print(f"{name} not found in the address book.")
    
    print("Redirecting to main menu...")

def write_contacts_to_file(filename):
    try:
      data = []
      for name, details in address_book.items():
          contact = {"Name": name}
          contact.update(details)
          data.append(contact)
    
      df = pd.DataFrame(data)
      # Save to CSV without row indices
      df.to_csv(filename, index=False)
      print(f"Contacts saved to '{filename}' successfully!")
      
    except PermissionError:
        print("Error: Permission denied to write to file.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def save_contacts_to_file():
    if not address_book:
        print("No contacts to save. Redirecting to main menu...")
        return

    while True:
        choice = input("Do you want to create a new file [1] or save to an existing file [2]? ").strip()
        if choice == '1':
            file_name = input_file_name()
            write_contacts_to_file(file_name)
            break
        elif choice == '2':
            file_name = input_file_name()
            if os.path.exists(file_name):
                overwrite = confirm_input(f"Overwrite {file_name}? (yes/no): ")
                if overwrite:
                 write_contacts_to_file(file_name)
                 return
                else:
                    print("saving cancelled")
                    break
            else:
                print("File does not exist.")
                try_again = confirm_input("Try entering the file name again? (yes/no): ")
                if not try_again:
                    print("redirecting to main menu....")
                    return
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Main function to interact with the address book
def main():
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Create/Save to File")
        print("5. Edit Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            while True:
                name = input_name("Enter contact name : ")
                phone = input_phone("Enter phone number : ")
                email = input_email("Enter email address (press [Enter] if none): ")
                job = get_input("Enter job title (press [Enter key] if none) : ")
                address = get_input("Enter address (press [Enter key] if none) : ")
                website = input_website("Enter website (press [Enter key] if none) : ")
                add_contact(name, phone, email, job, address, website)

                add_another = confirm_input("Do you want to add another contact? [yes/no]: ")
                if add_another == 'yes':
                    continue
                else:
                    print("redirecting to main menu...")
                    break


                    

        elif choice == '2':
            view_contacts()

        elif choice == '3':
             delete_contact()

        elif choice == '4':
            save_contacts_to_file()

        elif choice == '5':
            edit_contact()

        elif choice == '6':
            exit_confirm = confirm_input("Are you sure you want to exit? [yes/no]: ")
            if exit_confirm == 'yes':
                print("Exiting the address book. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
