The `Book` class models a library book with private attributes for title, author, genre, publication date, and borrowing status, ensuring encapsulation. It includes methods to get book details, check availability, borrow, and return the book. The `__str__` method provides a user-friendly string representation of the book's details and status (Available or Borrowed). This class enforces proper borrowing rules and maintains data integrity in a library management system.
    
    class Book:
        def __init__(self, title, author, genre, publication_date):
            self.__title = title
            self.__author = author
            self.__genre = genre
            self.__publication_date = publication_date
            self.__is_borrowed = False
    
        # Getters and Setters for private attributes
        def get_title(self):
            return self.__title
    
        def get_author(self):
            return self.__author
    
        def is_available(self):
            return not self.__is_borrowed
    
        def borrow(self):
            if self.__is_borrowed:
                return False
            self.__is_borrowed = True
            return True
    
        def return_book(self):
            self.__is_borrowed = False
    
        def __str__(self):
            status = "Available" if not self.__is_borrowed else "Borrowed"
            return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Published: {self.__publication_date}, Status: {status}"
    
The `User` class models a library user with private attributes for their name, library ID, and a list of borrowed books, ensuring encapsulation. It includes methods to get user details, borrow books (by adding titles to the borrowed list), return books (by removing titles from the list), and view the list of borrowed books. This class is essential for tracking user activity in a library management system.

    class User:
        def __init__(self, name, library_id):
            self.__name = name
            self.__library_id = library_id
            self.__borrowed_books = []
    
        # Getters and Setters
        def get_name(self):
            return self.__name
    
        def get_library_id(self):
            return self.__library_id
    
        def borrow_book(self, book_title):
            self.__borrowed_books.append(book_title)
    
        def return_book(self, book_title):
            if book_title in self.__borrowed_books:
                self.__borrowed_books.remove(book_title)
    
        def get_borrowed_books(self):
            return self.__borrowed_books
    
        def __str__(self):
            borrowed_books = ', '.join(self.__borrowed_books) if self.__borrowed_books else "No books borrowed"
            return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {borrowed_books}"
    

The `Author` class represents an author with attributes for their name and biography. It includes methods to access these attributes, allowing for the retrieval of the author's name and biography. This class is useful for managing and displaying author information in a library system.
    
    class Author:
        def __init__(self, name, biography):
            self.__name = name
            self.__biography = biography
    
        def get_name(self):
            return self.__name
    
        def get_biography(self):
            return self.__biography
    
        def __str__(self):
            return f"Name: {self.__name}, Biography: {self.__biography}"


The LibrarySystem class is a fully functional application designed to handle various library operations. It stores books, users, and authors as separate lists,
providing methods to manage these entities through different actions:
    -Book Operations: Users can add new books, borrow and return books,
search for books by title, and display all available books.
    -User Operations: The system supports adding new users,
viewing user details by name, and displaying all users.
    -Author Operations: Users can add new authors,
view author details, and display all authors in the system.

The class uses encapsulation to manage the state of books, users, and authors. Each method ensures that only valid data is added or manipulated within the system, with appropriate messages for user feedback. The run() method provides a main loop that continuously presents the user with the main menu, directing them to the respective operation menus (book, user, author) or allowing them to quit the system.

Each operation is organized into separate methods, such as add_book() for adding books and borrow_book() for borrowing, which promote code modularity and maintainability. The __str__ methods in the Book, User, and Author classes provide a readable string representation, making it easier to display information to the user.

    class LibrarySystem:
        def __init__(self):
            self.books = []
            self.users = []
            self.authors = []
    
        def add_book(self):
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date: ")
            book = Book(title, author, genre, publication_date)
            self.books.append(book)
            print("Book added successfully!")
    
        def borrow_book(self):
            title = input("Enter the title of the book to borrow: ")
            user_name = input("Enter your name: ")
            for book in self.books:
                if book.get_title().lower() == title.lower() and book.is_available():
                    for user in self.users:
                        if user.get_name().lower() == user_name.lower():
                            if book.borrow():
                                user.borrow_book(title)
                                print(f"{title} borrowed successfully!")
                            return
            print(f"Book '{title}' is not available or user not found.")
    
        def return_book(self):
            title = input("Enter the title of the book to return: ")
            user_name = input("Enter your name: ")
            for book in self.books:
                if book.get_title().lower() == title.lower() and not book.is_available():
                    for user in self.users:
                        if user.get_name().lower() == user_name.lower():
                            book.return_book()
                            user.return_book(title)
                            print(f"{title} returned successfully!")
                            return
            print("Return operation failed. Book or user not found.")
    
        def search_book(self):
            title = input("Enter book title to search: ")
            for book in self.books:
                if book.get_title().lower() == title.lower():
                    print(book)
                    return
            print("Book not found.")
    
        def display_books(self):
            if not self.books:
                print("No books in the library.")
            else:
                for book in self.books:
                    print(book)
    
        def add_user(self):
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(name, library_id)
            self.users.append(user)
            print("User added successfully!")
    
        def view_user_details(self):
            name = input("Enter user name: ")
            for user in self.users:
                if user.get_name().lower() == name.lower():
                    print(user)
                    return
            print("User not found.")
    
        def display_users(self):
            if not self.users:
                print("No users in the system.")
            else:
                for user in self.users:
                    print(user)
    
        def add_author(self):
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            self.authors.append(author)
            print("Author added successfully!")
    
        def view_author_details(self):
            name = input("Enter author name: ")
            for author in self.authors:
                if author.get_name().lower() == name.lower():
                    print(author)
                    return
            print("Author not found.")
    
        def display_authors(self):
            if not self.authors:
                print("No authors in the system.")
            else:
                for author in self.authors:
                    print(author)
    
        def run(self):
            while True:
                print("\nWelcome to the Library Management System!")
                print("1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
                choice = input("Select an option: ")
                if choice == "1":
                    self.book_menu()
                elif choice == "2":
                    self.user_menu()
                elif choice == "3":
                    self.author_menu()
                elif choice == "4":
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid option.")
    
        def book_menu(self):
            print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.display_books()
            else:
                print("Invalid option.")
    
        def user_menu(self):
            print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.view_user_details()
            elif choice == "3":
                self.display_users()
            else:
                print("Invalid option.")
    
        def author_menu(self):
            print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
            choice = input("Select an option: ")
            if choice == "1":
                self.add_author()
            elif choice == "2":
                self.view_author_details()
            elif choice == "3":
                self.display_authors()
            else:
                print("Invalid option.")
    
    
    if __name__ == "__main__":
        system = LibrarySystem()
        system.run()
