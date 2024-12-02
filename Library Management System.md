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