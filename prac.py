class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title}, Author: {self.author}, ISBN: {self.isbn}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
                break
        
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book '{book_to_remove.title}' removed from the library.")
        else:
            print("Book not found.")

    def search_books_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def display_books(self):
        if self.books:
            print("Books in library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")
            # Example usage:
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

library.add_book(book1)
library.add_book(book2)

library.display_books()

print("Search by title 'great':")
for book in library.search_books_by_title("great"):
    print(book)

library.remove_book("9780743273565")
library.display_books()

