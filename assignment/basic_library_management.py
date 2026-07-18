class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}")
    def update_year(self, new_year):
        self.year = new_year
    def update_author(self, new_author):
        self.author = new_author
    def update_title(self, new_title):
        self.title = new_title
    
    
class Library:
    def __init__(self):
        self.books = dict()
    def add_book(self, book:Book):
        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book]+=1
    def remove_book(self, book:Book):
        if book in self.books:
            if self.books[book] > 0:
                self.books[book]-=1
            else:
                print("All loaned!")
        else:
            print("Book not found in library.")
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book, self.books[book]
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Copies: {self.books[book]}")

print("LIBRARY MANAGEMENT SYSTEM")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

wrc_lib = Library()
wrc_lib.add_book(book1)
wrc_lib.add_book(book2)
print("\nALL BOOKS")
wrc_lib.display_books()
print("\nPARTICULAR BOOK")
found_book, book_count = wrc_lib.search_book("To Kill a Mockingbird")

found_book.display()
