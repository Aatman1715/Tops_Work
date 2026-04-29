#Code to create a Book class with attributes like ISBN, title, author, and genre. The class should have a method to display the details of the book, and take multiple inputs as a list from the user to create objects of the Book class and display its details.
class Book:
    def __init__(self, isbn, title, author, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre

    def display_details(self):
        print(f"Book Details:")
        print(f"ISBN: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
books = []
num_books = int(input("Enter the number of books you want to add: "))
for _ in range(num_books):
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    book = Book(isbn, title, author, genre)
    books.append(book)
for book in books:
    book.display_details()
    print() 