import time

# Challenge 1
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} on (ISBN: {self.isbn})"

# Challenge 2
class Ebook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return f"{self.title} by {self.author} on (ISBN: {self.isbn}) - Format: {self.file_format}"

# Challenge 3
class Library:
    def __init__(self):
        self.books = []

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < len(self.books):
            x = self.books[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        book_to_remove = next((b for b in self.books if book_title in b.title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
        else:
            print(f"Book titled '{book_title}' not found in the library.")

    def __str__(self):
        if not self.books:
            return "The library is empty."
        result = "Library Books:\n"
        for i, book in enumerate(self.books, 1):
            result += f"{i}. {book}\n"
        return result


import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="605166",
            database="librarydb"
        )
        self.cur = self.mydb.cursor()
        self.books = []

    def save_book(self, book):
        
        if isinstance(book, Ebook):
            sql = "INSERT INTO book (title, author, isbn, file_format) VALUES (%s, %s, %s, %s)"
            val = (book.title, book.author, book.isbn, book.file_format)
        else:
            sql = "INSERT INTO book (title, author, isbn) VALUES (%s, %s, %s)"
            val = (book.title, book.author, book.isbn)
        
        self.cur.execute(sql, val)
        self.mydb.commit()
        
        print(f"Book '{book.title}' saved to database.")
        
    def load_books(self):
        self.cur.execute("SELECT title, author, isbn, file_format FROM book")
        rows = self.cur.fetchall()
        self.cur.rem
        books = []
        for row in rows:
            title, author, isbn, file_format = row
            if file_format:
                books.append(Ebook(title, author, isbn, file_format))
            else:
                books.append(Book(title, author, isbn))
        return books
    
    def __str__(self):
        if not self.books:
            return "No books found."
        else:
            return "\n".join(str(book) for book in self.books)

    
# Connect to server
    # mydb = mysql.connector.connect(
    #     host="127.0.0.1",
    #     port=3306,
    #     user="root",
    #     password="605166")
    
    # print(mydb)

    # # Get a cursor
    # cur = mydb.cursor()

    # CREATE DATABASE
    # cur.execute("CREATE DATABASE IF NOT EXISTS librarydb")
    
    # USE DATABASE
    # cur.execute("USE librarydb")
    
    # CREATE TABLE book
    # cur.execute("""
    #         CREATE TABLE book (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             title VARCHAR(255) NOT NULL,
    #             author VARCHAR(255) NOT NULL,
    #             isbn VARCHAR(20) NOT NULL,
    #             file_format VARCHAR(20)
    #         )
    #     """)
if __name__ == '__main__':
    library = Library()
    mydb = DatabaseManager()

    while True:
        print("\n" + "="*30)
        print(" LIBRARY MANAGEMENT SYSTEM ")
        print("="*30)
        print("\n1. Check all Books\n2. Add a book\n3. Save books to DB\n4. Load books from DB\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("="*30)
            print(" ALL BOOKS IN LIBRARY ")
            print("="*30)
            time.sleep(0.5)
            
            print(library)  # This uses the __str__ method
            time.sleep(1.5)
            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            print("="*30)
            print(" ADD A NEW BOOK ")
            print("="*30)
            
            time.sleep(0.5)
            
            # Input validation for book details
            while True:
                book_title = input("Book Title: ").strip()
                if book_title:
                    break
                print("Title cannot be empty! Please try again.")
            
            while True:
                book_author = input("Book Author: ").strip()
                if book_author:
                    break
                print("Author cannot be empty! Please try again.")
            
            while True:
                book_isbn = input("Book ISBN: ").strip()
                if book_isbn:
                    break
                print("ISBN cannot be empty! Please try again.")
            
            # Check if it's an ebook or physical book
            while True:
                book_type = input("Is this an ebook? (y/n): ").strip().lower()
                if book_type in ['y', 'yes']:
                    while True:
                        book_format = input("Book Format (PDF, EPUB, MOBI, etc.): ").strip()
                        if book_format:
                            new_book = Ebook(book_title, book_author, book_isbn, book_format)
                            break
                        print("Book format cannot be empty! Please try again.")
                    break
                elif book_type in ['n', 'no']:
                    new_book = Book(book_title, book_author, book_isbn)
                    break
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            
            library.add_book(new_book)
            print(f"\n✅ Book added successfully!")
            print(f"Added: {new_book}")  # This uses the Book's __str__ method
            
            time.sleep(1.5)
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            print("="*30)
            print(" SAVE BOOKS IN THE DATABASE! ")
            print("="*30)
            
            time.sleep(0.5)
            
            if not library.books:
                print("No books to save. Please add books first.\n")
            else:
                mydb.save_book(library.books[-1])  # Save the last added book
                
        elif choice == "4":
            print("="*30)
            print(" LOAD BOOKS FROM THE DATABASE ")
            print("="*30)
            
            time.sleep(0.5)

            if not library.books:
                print("No books to load. Please add books first.\n")
            else:
                books = mydb.load_books()
                for book in books:
                    print(book)
                print("\n✅ Books loaded successfully!")
            
        else:
            print("❌ Invalid choice! Please select 1, 2, 3, 4, or 5.")
            time.sleep(1)
            input("\nPress Enter to return to the menu...")
