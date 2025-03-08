import re
def input_name(prompt):
    name_pattern = r'^(?!\d)[\w\s\-\'À-ÿ]+$'  # Allows international characters and apostrophes
    while True:
        name = input(prompt).strip()
        if re.match(name_pattern, name, re.UNICODE):
            return name.title()  # Standardize capitalization
        print("Invalid name! Only letters, spaces, hyphens, and apostrophes allowed.")

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return self.name


class Book:
    def __init__(self, title, authors, topic, category):
        self._title = title
        self._authors = authors  # List of Author objects
        self._topic = topic
        self._category = category
        self._is_checked_out = False

        # Add this book to each author's bibliography
        for author in authors:
            author.add_book(self)

    @property
    def title(self):
        return self._title

    @property
    def authors(self):
        return self._authors

    @property
    def topic(self):
        return self._topic

    @property
    def category(self):
        return self._category

    @property
    def is_checked_out(self):
        return self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {', '.join(str(author) for author in self.authors)}"


class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._checked_out_books = []

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def name(self):
        return self._name

    @property
    def checked_out_books(self):
        return self._checked_out_books

    def add_checked_out_book(self, book):
        self._checked_out_books.append(book)

    def remove_checked_out_book(self, book):
        if book in self._checked_out_books:
            self._checked_out_books.remove(book)


class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Book '{book.title}' added to library by librarian {self.name}")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"Book '{book.title}' removed from library by librarian {self.name}")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def search_books(self, search_term, fields=['title', 'author', 'topic', 'category']):
        """
        Flexible search with partial matching across specified fields
        """
        search_term = search_term.lower()
        results = []
        
        for book in self.books:
            match = False
            
            # Check each requested field
            if 'title' in fields and search_term in book.title.lower():
                match = True
            elif 'author' in fields and any(search_term in author.name.lower() for author in book.authors):
                match = True
            elif 'topic' in fields and search_term in book.topic.lower():
                match = True
            elif 'category' in fields and search_term in book.category.lower():
                match = True
            
            if match:
                results.append(book)
        
        return results

    def checkout_book(self, user, book):
        if user not in self.users:
            print("Error: User not registered in library")
            return False
        if book not in self.books:
            print("Error: Book not found in library")
            return False
        if book.is_checked_out:
            print("Error: Book already checked out")
            return False

        book.check_out()
        user.add_checked_out_book(book)
        print(f"Book '{book.title}' checked out to {user.name}")
        return True

    def return_book(self, user, book):
        if book not in user.checked_out_books:
            print("Error: This book wasn't checked out by this user")
            return False

        book.return_book()
        user.remove_checked_out_book(book)
        print(f"Book '{book.title}' returned by {user.name}")
        return True

def display_books(books):
    print("\nSearch Results:")
    for i, book in enumerate(books, 1):
        status = "Checked Out" if book.is_checked_out else "Available"
        print(f"{i}. {book.title} by {', '.join(str(a) for a in book.authors)} ({status})")

def get_user_details(library):
    print("\nWelcome to the Library System!")
    name = input_name("Enter your full name: ")
    user_id = input_name("Choose a username: ")
    
    # Check if user already exists
    existing_user = next((u for u in library.users if u.user_id == user_id), None)
    if existing_user:
        print(f"Welcome back, {existing_user.name}!")
        return existing_user
    
    new_user = User(user_id, name)
    library.add_user(new_user)
    print(f"New user created: {name} ({user_id})")
    return new_user

def handle_search_flow(library, search_fields, prompt_message):
    """Generic reusable function for search operations with retry logic"""
    while True:
        search_term = input(f"\n{prompt_message} (or press Enter to cancel): ").strip()
        if not search_term:
            return None  # User cancelled

        results = library.search_books(search_term, search_fields)
        display_books(results)

        if not results:
            print("\nNo matching books found.")
            retry = input("Would you like to:"
                          "\n1. Try another search"
                          "\n2. Return to main menu"
                          "\nEnter choice (1-2): ").strip()
            
            if retry == '1':
                continue
            elif retry == '2':
                return None
            else:
                print("Invalid choice, returning to main menu.")
                return None
        else:
            return results

def main_menu(library, user):
    while True:
        print("\nMain Menu:")
        print("1. Search for a book")
        print("2. Checkout a book")
        print("3. Return a book")
        print("4. View my checked out books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\nSearch Options:")
            print("1. Title")
            print("2. Author")
            print("3. Topic")
            print("4. Category")
            print("5. All Fields")
            search_choice = input("Choose search scope (1-5): ").strip()
            
            fields_map = {
                '1': ['title'],
                '2': ['author'],
                '3': ['topic'],
                '4': ['category'],
                '5': ['title', 'author', 'topic', 'category']
            }
            
            fields = fields_map.get(search_choice, ['title', 'author', 'topic', 'category'])
            results = handle_search_flow(
                library,
                fields,
                f"Enter search term for {', '.join(fields).title()}"
            )
            
            if results:
                display_books(results)

        elif choice == '2':
            results = handle_search_flow(
                library,
                ['title'],
                "Enter title of book to checkout"
            )
            
            if results:
                try:
                    selection = int(input("Enter number of book to checkout (0 to cancel): "))
                    if 1 <= selection <= len(results):
                        selected_book = results[selection-1]
                        if library.checkout_book(user, selected_book):
                            print("Checkout successful!")
                    elif selection != 0:
                        print("Invalid selection!")
                except ValueError:
                    print("Please enter a valid number!")

        elif choice == '3':
            if not user.checked_out_books:
                print("You have no books to return!")
                continue
                
            print("\nBooks you've checked out:")
            for i, book in enumerate(user.checked_out_books, 1):
                print(f"{i}. {book.title}")
            
            try:
                selection = int(input("Enter number of book to return (0 to cancel): "))
                if 1 <= selection <= len(user.checked_out_books):
                    selected_book = user.checked_out_books[selection-1]
                    if library.return_book(user, selected_book):
                        print("Return successful!")
                elif selection != 0:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == '4':
            if not user.checked_out_books:
                print("You have no books checked out!")
                continue
                
            print("\nYour checked out books:")
            for i, book in enumerate(user.checked_out_books, 1):
                print(f"{i}. {book.title}")

        elif choice == '5':
            print("Thank you for using the library system!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-5.")
# Example Usage
if __name__ == "__main__":
    # Setup initial library data
    library = Library()
    
    # Create sample authors and books
    rowling = Author("J.K. Rowling")
    orwell = Author("George Orwell")

    
    harry_potter = Book("Harry Potter", [rowling], "Magic", "Fantasy")
    harry_potter_2 = Book("Harry potter 2", [rowling], "Magic", "Fantasy")
    harry_potter_3 = Book("Harry potter 3", [rowling], "Magic", "Fantasy")
    nineteen_eighty_four = Book("1984", [orwell], "Dystopia", "Fiction")
    animal_farm = Book("Animal Farm", [orwell], "Politics", "Satire")
    
    library.add_book(harry_potter)
    library.add_book(harry_potter_2)
    library.add_book(harry_potter_3)
    library.add_book(nineteen_eighty_four)
    library.add_book(animal_farm)
    
    # Create a librarian
    librarian = Librarian("lib1", "Bob Smith")
    library.add_user(librarian)
    
    # Start user interaction
    user = get_user_details(library)
    main_menu(library, user)